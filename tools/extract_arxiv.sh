#!/bin/bash
# Description: Download arXiv bundle, extract it, convert PDFs using qlmanage, and run parser in Docker.
# Usage: ./tools/extract_arxiv.sh <arxiv_id> <task_name> [topic_dir]
# Example: ./tools/extract_arxiv.sh 2502.15685 "Active Large Language Model-based Knowledge Distillation" "LLMを用いたレコメンドモデルの蒸留技術"

# Stop on first error
set -e

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <arxiv_id> <task_name> [topic_dir]"
    exit 1
fi

ARXIV_ID=$1
TASK_NAME=$2
TOPIC_DIR="${3:-LLMを用いたレコメンドモデルの蒸留技術}"

ROOT_DIR=$(pwd)
BASE_DIR="${ROOT_DIR}/${TOPIC_DIR}/article_summaries/${TASK_NAME}"
SOURCE_DIR="${BASE_DIR}/source"
IMAGES_DIR="${BASE_DIR}/images"

echo "Creating directories..."
mkdir -p "$SOURCE_DIR" "$IMAGES_DIR"

echo "Downloading source and PDF..."
curl -sL "https://arxiv.org/e-print/${ARXIV_ID}" -o "${SOURCE_DIR}/source.tar.gz"
curl -sL "https://arxiv.org/pdf/${ARXIV_ID}.pdf" -o "${SOURCE_DIR}/paper.pdf"

echo "Extracting source..."
# Temporarily disable stop on error because some tar files have harmless symlink warnings
set +e
tar -xzf "${SOURCE_DIR}/source.tar.gz" -C "$SOURCE_DIR"
set -e

echo "Converting PDF images using qlmanage..."
# Find all PDF files inside the extracted source (excluding the main paper.pdf)
find "${SOURCE_DIR}" -type f -name "*.pdf" | grep -v "paper.pdf" | while read -r pdf_path; do
    filename=$(basename -- "$pdf_path")
    filename_noext="${filename%.*}"
    # Convert PDF to PNG using qlmanage
    qlmanage -t -s 1200 -o "${IMAGES_DIR}" "$pdf_path" >/dev/null 2>&1
    
    # Rename generated file `foo.pdf.png` to `foo.png` for easier markdown linking
    mv "${IMAGES_DIR}/${filename_noext}.pdf.png" "${IMAGES_DIR}/${filename_noext}.png" 2>/dev/null || true
    mv "${IMAGES_DIR}/${filename}.png" "${IMAGES_DIR}/${filename_noext}.png" 2>/dev/null || true
done

echo "Copying native images (PNG/JPG)..."
find "${SOURCE_DIR}" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \) | while read -r img_path; do
    cp "$img_path" "${IMAGES_DIR}/"
done

echo "Converting EPS images using Ghostscript via Docker..."
eps_count=$(find "${SOURCE_DIR}" -type f -iname "*.eps" | wc -l | tr -d ' ')
if [ "$eps_count" -gt 0 ]; then
    REL_OUT="${IMAGES_DIR#${ROOT_DIR}/}"
    REL_SRC="${SOURCE_DIR#${ROOT_DIR}/}"
    docker compose run --rm python bash -c "apt-get update -qq && apt-get install -y -qq ghostscript && for f in /workspace/${REL_SRC}/*.eps; do gs -dSAFER -dBATCH -dNOPAUSE -dEPSCrop -sDEVICE=png16m -r300 -sOutputFile=/workspace/${REL_OUT}/\$(basename \$f .eps).png \$f; done"
fi

echo "Running Python parser via Docker..."
# Identify the main .tex and .bbl files
MAIN_TEX=$(find "${SOURCE_DIR}" -maxdepth 2 -name "*.tex" | head -n 1)
MAIN_BBL=$(find "${SOURCE_DIR}" -maxdepth 2 -name "*.bbl" | head -n 1)

if [ -n "$MAIN_TEX" ]; then
    # We use relative paths from the root for Docker bind mounts mapping correctly to /workspace
    # If the user is running bash, we use simple parameter substring removal or relative paths
    # Because Mac natively doesn't have `realpath --relative-to`, we do simple replacement
    REL_TEX="${MAIN_TEX#${ROOT_DIR}/}"
    if [ -n "$MAIN_BBL" ]; then
        REL_BBL="${MAIN_BBL#${ROOT_DIR}/}"
    else
        REL_BBL=""
    fi
    REL_OUT="${BASE_DIR#${ROOT_DIR}/}"
    
    docker compose run --rm python python tools/arxiv_parser.py --tex "$REL_TEX" --bbl "$REL_BBL" --outdir "$REL_OUT"
else
    echo "Warning: No .tex file found. Cannot run parser."
fi

echo ""
echo "Extraction and parsing complete! Targets in:"
echo "Images: $IMAGES_DIR"
echo "Tables/Refs: $BASE_DIR"
