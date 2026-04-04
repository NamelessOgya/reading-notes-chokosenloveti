## **Do We Really Need Specialization? Evaluating Generalist Text Embeddings for Zero-Shot Recommendation and Search** 

MATTEO ATTIMONELLI, Politecnico Di Bari, Italy and Sapienza University of Rome, Italy ALESSANDRO DE BELLIS, Politecnico Di Bari, Italy 

CLAUDIO POMO, Politecnico Di Bari, Italy 

DIETMAR JANNACH, University of Klagenfurt, Austria 

EUGENIO DI SCIASCIO, Politecnico Di Bari, Italy 

## TOMMASO DI NOIA, Politecnico Di Bari, Italy 

Pre-trained language models (PLMs) are widely used to derive semantic representations from item metadata in recommendation and search. In sequential recommendation, PLMs enhance ID-based embeddings through textual metadata, while in product search, they align item characteristics with user intent. Recent studies suggest task and domain-speci!c !ne-tuning are needed to improve representational power. This paper challenges this assumption, showing that _Generalist Text Embedding Models (GTEs)_ , pre-trained on large-scale corpora, can guarantee strong zero-shot performance without specialized adaptation. Our experiments demonstrate that GTEs outperform traditional and !ne-tuned models in both sequential recommendation and product search. We attribute this to a superior representational power, as they distribute features more evenly across the embedding space. Finally, we show that compressing embedding dimensions by focusing on the most informative directions (e.g., via PCA) e"ectively reduces noise and improves the performance of specialized models. To ensure reproducibility, we provide our repository at https://split.to/gte4ps. 

CCS Concepts: • **Do Not Use This Code** → **Generate the Correct Terms for Your Paper** ; _Generate the Correct Terms for Your Paper_ ; Generate the Correct Terms for Your Paper; Generate the Correct Terms for Your Paper. 

Additional Key Words and Phrases: Sequential Recommendation, Product Search, Generalist Text Embedding Models 

## **1 Introduction** 

Recommendation and Search systems are essential for helping users navigate large information spaces, from retrieving relevant documents to providing personalized product suggestions. Traditional methods often rely on ID-based embeddings or keyword-based matching, which may struggle to capture the nuanced semantics of user intent and item content, especially in cold-start scenarios. Recent advances in Natural Language Processing, especially the rise of pretrained language models (PLMs), have created new opportunities for tackling these challenges. PLMs like BERT [5] and T5 [28] move beyond shallow matching by capturing rich representations of queries, items, and users. In recommendation, particularly in sequential settings, they enhance item embeddings by modeling content and user behavior dynamics [11, 36]; in search, they improve query-item alignment. Despite their bene!ts, PLMs are not directly optimized for recommendation and search tasks, often limiting generalization [10]. Recent work has addressed this through task-speci!c !ne-tuning. One notable example is BL!IR [10], a RoBERTa [20]-based embedding model, !ne-tuned on large-scale user reviews and item metadata to better align query and item embeddings, improving e#cacy in sequential recommendation and product search. While domain and task adaptation methods such as BL!IR highlight their bene!ts of specialized models, recent advances in text embedding techniques have led to the emergence of _Generalist Text_ 

Authors’ Contact Information: Matteo Attimonelli, matteo.attimonelli@poliba.it, Politecnico Di Bari, Bari, Italy and Sapienza University of Rome, Rome, Italy; Alessandro De Bellis, alessandro.debellis@poliba.it, Politecnico Di Bari, Bari, Italy; Claudio Pomo, claudio.pomo@poliba.it, Politecnico Di Bari, Bari, Italy; Dietmar Jannach, dietmar.jannach@aau.at, University of Klagenfurt, Klagenfurt, Austria; Eugenio Di Sciascio, eugenio.disciascio@poliba.it, Politecnico Di Bari, Bari, Italy; Tommaso Di Noia, tommaso.dinoia@poliba.it, Politecnico Di Bari, Bari, Italy. 

1 

Attimonelli et al. 

2 

_Embedding Models (GTEs)_ [17, 19]. Trained on diverse corpora and tasks, GTEs learn broad, transferable semantics, o"ering a training-free alternative to !ne-tuning at scale. Thus, they may o"er a strong alternative as embedding models for recommendation and search, achieving competitive performance without speci!c adaptation. 

This motivates the main research question in this paper: **How well do GTEs perform in recommendation and search tasks in a zero-shot setting, compared to traditional and !ne-tuned models?** To address this question, we evaluate state-of-the-art GTEs on two key tasks: _sequential recommendation_ and _product search_ , focusing on models included in the _Massive Text Embedding Benchmark (MTEB)_ [24]. Our results show that GTEs outperform both traditional and !ne-tuned models, with recent open-source models (e.g., NVEmbed-v2 [17] and GTE-Qwen2 [19]) even surpassing popular closed-source alternatives such as OpenAI’s. 

Moreover, our study takes a !rst step towards addressing a largely open question: _What underlying characteristics of textual embeddings in!uence their e"ectiveness for recommendation and search?_ We focus on factors related to embedding geometry and dimensionality, aiming to uncover the key characteristics that govern embedding e"ectiveness. In particular, we analyze _space utilization_ , examining how e"ectively models distribute variance across embedding dimensions, addressing concerns about _dimensional collapse_ [6]. We use PCA to estimate the _e"ective dimensionality_ , providing a quantitative measure of the phenomenon. This analysis reveals that GTEs tend to achieve more uniform space utilization. Building on this, we demonstrate that PCA itself provides a pathway for e"ective compression: retaining only the most informative components substantially reduces GTE dimensionality without sacri!cing accuracy, thus improving scalability. We further !nd that this compression also bene!ts !ne-tuned models, removing noisy dimensions and reducing the performance gap compared to GTEs. 

The rest of the paper is organized as follows: Section 2 provides an overview of related work, Section 3 describes the methodology and tasks, Section 4 presents the experimental setup and results, and Section 5 concludes the paper with a discussion of future directions. 

## **2 Related Work** 

_Generalist Text Embedding Models._ GTEs [19] are text embedding models trained on large-scale corpora and diverse tasks to produce rich, transferable representations for a variety of downstream applications. Several encoder-based GTEs build on the transformer encoder [5] architecture. For instance, mGTE [39] extends BERT [5] with RoPE [33] and unpadding [27] for long-context support. I"#$%&’$OR [32] enhances GTR [26] via instruction tuning for task-aware embeddings, while Sentence-T5 [25] derives embeddings from the T5 [28] encoder block. Decoder-only LLMs have also been adapted for embedding tasks. GTE-Qwen2 [19] repurposes Qwen2 [35] via multi-stage training to generate universal embeddings. Jasper [37] applies Matrioshka Representation Learning [16] to distill embeddings from a larger teacher model. NVEmbed-v2 [17], based on Mistral-7B [13], removes causal masking and introduces latent attention for improved token-aware pooling. KALM [12], being !ne-tuned on a small model (i.e., Qwen2-0.5B), shows that even compact models can yield high-quality embeddings when trained on large-scale, multi-task datasets. 

_Text Encoders for Sequential Recommendation and Product Search._ Sequential recommendation predicts a user’s next interaction based on past behavior. Transformer-based models (e.g., SASRec [14] and BERT4Rec [34]) address the limitations of recurrent models such as GRU4Rec [9], employing self-attention for long-range dependencies and parallelization. Yet, many approaches rely solely on item IDs, ignoring side information like metadata and images. UniSRec [11] demonstrates the e"ectiveness of incorporating multimodal signals, combining ID and semantic features [36]. Unlike recommendation, product search requires explicit query-item matching. Traditional methods (e.g., BM25) have 

Do We Really Need Specialization? Evaluating GTEs for Zero-Shot Recommendation and Search 

3 

been supplanted by deep models that learn dense query and product embeddings. Transformer-based approaches like BERT [5] and ColBERT [15] enhance semantic matching but face limitations due to a certain scarcity of public datasets [22, 23]. To address this, BL!IR [10] introduces a contrastive learning-based text encoder using reviews as pseudo-queries. Still, most text embedding solutions in recommendation and search rely on closed-source models [3, 8] or domain-speci!c !ne-tuning (e.g., BL!IR) leaving GTEs largely unexplored. 

_Embedding Quality Evaluation._ Embedding models are commonly evaluated implicitly through downstream task performance. MTEB 

[24] provides a comprehensive suite for assessing the performance of GTEs across such tasks. Beyond downstream performance, it is also crucial to investigate the intrinsic properties of embedding models, as these can signi!cantly in$uence their e"ectiveness and suitability in practical applications. Factors such as embedding dimension and model capacity a"ect not only accuracy but also the scalability and sustainability of retrieval systems [16]. Another key aspect is space utilization: a frequent issue in contextual pre-trained language models is _dimensional collapse_ [6, 7], where embeddings lie in low-rank subspaces, limiting expressiveness and degrading performance [21] in tasks reliant on distance metrics [25]. Consequently, post-processing methods [18, 38] have been proposed to improve embedding utility. In this work, we investigate whether GTEs inherently possess properties that enable e#cient space utilization, potentially eliminating the need for ad-hoc adaptation. 

## **3 Background and Methodology** 

This section outlines our methodology and formalizes two core tasks: sequential recommendation and product search. 

## **3.1 Task Overview** 

_3.1.1 Sequential Recommendation (SR)._ Sequential recommendation focuses on modeling a user’s evolving interests based on their interaction history, with the goal of predicting the next item of interest. Let a user session be represented as a sequence S _𝐿_ = [ _𝐿_ 1 _,𝐿_ 2 _, . . . ,𝐿𝐿_ ] _, 𝐿 𝑀_ ↑I, where I is the set of all items, and _𝐿 𝑀_ denotes the item interacted with at position _𝑀_ . The recommendation task can be framed as learning a function _𝑁_ seq (S _𝐿_ ) → _𝐿𝐿_ +1. Recent approaches employ neural sequence models to encode the interaction sequence. Each item _𝐿 𝑀_ is mapped to an embedding e _𝑁 𝐿_ ↑ R _[𝑂]_ using an item encoder e _𝑁_ , and a sequence encoder _𝑂_ seq transforms the embedded sequence into a contextual representation h _𝐿_ = _𝑂_ seq ([e _𝑁_ 1 _,_ e _𝑁_ 2 _, . . . ,_ e _𝑁𝑀_ ]), where h _𝐿_ ↑ R _[𝑂]_ captures the user’s dynamic preference at time _𝑃_ . This representation h _𝐿_ is then used to score or rank the candidate items via a similarity measure, Sim(· _,_ ·), as _𝑁_ seq (S _𝐿_ ) = arg max _𝑁_ ↑I Sim(h _𝐿 ,𝑂𝑃_ ( _𝐿_ )). 

_3.1.2 Product Search (PS)._ Product search aims to retrieve the most relevant items from a large catalog I = { _𝐿_ 1 _,𝐿_ 2 _, . . . ,𝐿𝑄_ } in response to a user query _𝑄_ ↑Q (the space of possible queries), often expressed in natural language. Recent approaches signi!cantly improve upon traditional lexical matching (e.g., BM25) by leveraging PLMs to map queries and items into a shared high-dimensional embedding space. A pre-trained text embedding model generates dense vector representations e _𝑅_ for queries and e _𝑁_ for items, typically using their textual attributes (like titles, descriptions, or metadata). The core task is to learn a scoring function _𝑁_ ( _𝑄,𝐿_ ) → R that re$ects the relevance of item _𝐿_ to query _𝑄_ . This score is commonly computed as the similarity between their respective embeddings: _𝑁_ ( _𝑄,𝐿_ ) = Sim(e _𝑅,_ e _𝑁_ ) where Sim(· _,_ ·) often represents cosine similarity or dot product. Items are then ranked according to this relevance score. 

Attimonelli et al. 

4 

## **3.2 Embedding Space Utilization** 

Text embedding models, which map text to dense representations, often su"er from _dimensional collapse_ [6], where variance concentrates in a small subset of dimensions. We use _e"ective dimensionality_ [4] to quantify this e"ect. Let E _[𝑆]_ I[↑][R] _[𝑄]_[↓] _[𝑂]_[denote the set of mean-centered item embeddings, extracted from a pre-trained encoder using item metadata.] Applying PCA yields singular values { _𝑅𝑁_ } _[𝑂] 𝑁_ =[↔] 0[1][for the covariance matrix of][ E] _[𝑆]_ I[. The] **[ explained variance ratio]**[ for the] top _𝑆_ components is de!ned as _𝑇𝑇_ =[�] _[𝑇] 𝑁_ =[↔] 0[1] _[𝑅][𝑁]_ �� _𝑂𝑁_ =↔01 _[𝑅][𝑁]_[. The] _[ 𝑈]_ **[-e"ective dimension]**[ is then] _[ 𝑉]_[(] _[𝑈]_[)][:][=][ arg min] _[𝑇][𝑇][𝑇]_[↗] _[𝑈]_[,] representing the minimum number of components needed to retain at least an _𝑈_ fraction of the total variance. Following prior work [4], we robustly estimate principal components by applying PCA to a random subset E[ˆ] _[𝑆]_ I[↑][R] _[𝑈]_[↓] _[𝑂]_[, where] _𝑊_ ↘ _𝑉_ [30]. Projecting query embeddings onto the resulting subspace ensures representational consistency, reduces dimensionality, and preserves the most discriminative features. This analysis (i) quanti!es **space utilization** [30], which impacts downstream performance [21], and (ii) establishes a **lower bound for compression** critical for scaling large GTEs while maintaining informativeness. 

## **4 Experiments and Discussion** 

We evaluate di"erent GTEs on sequential recommendation (SR) and product search (PS), as de!ned in Section 3.1, and analyze the properties of their embeddings in relation to performance. Our experiments address two core research questions: 

- **RQ1:** How well do GTEs perform in recommendation and search tasks in a zero-shot setting, compared to traditional and !ne-tuned models? 

- **RQ2:** What underlying characteristics of textual embeddings in$uence their e"ectiveness for recommendation and search? 

## **4.1 Experimental Setup** 

_4.1.1 Datasets._ To ensure fair comparison with prior work, we adopt the experimental con!guration of Hou et al. [10] for both SR and PS. We use the Amazon Reviews 2023 dataset [10], accessed via the HuggingFace[1] datasets API, following the original data splits and preprocessing. Item metadata is constructed by concatenating the _title_ , _features_ , _categories_ , and _description_ !elds. 

For SR, we focus on the _All Beauty_ (Beauty), _Video Games_ (Games), and _Baby Products_ (Baby) categories, with useritem interactions ranging from 104,766 to 3,583,323, re$ecting varying data sparsity. For PS, we use the ESCI [29] and Amazon-C4 [10] datasets. ESCI provides real-world <query,item> pairs with graded relevance labels. Following Hou et al. [10], we select only _exact_ matches from the English _ESCI-small_ split for higher-quality supervision, containing 27,643 queries and 1,367,729 items. Amazon-C4 comprises 21,223 queries and 1,058,417 items, with synthetic queries generated from 5-star reviews using ChatGPT [2]. Queries in both datasets are linked to Amazon Reviews 2023 via product IDs. We report results on two representative categories: _O#ce Products_ (O#ce) and _Sports and Outdoors_ (Sports). Following the evaluation protocol of Hou et al. [10], each <query,item> pair is ranked against a pool of 50 randomly sampled items for each domain. 

_4.1.2 Models._ For SR, we consider the baseline models GRU4Rec [9], SASRec [14], and UniSRec [11]. Both GRU4Rec and SASRec are designed to operate with item ID embeddings. To incorporate textual information, we follow the 

1https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023 

Do We Really Need Specialization? Evaluating GTEs for Zero-Shot Recommendation and Search 

5 

Table 1. Sequential recommendation performance: Recall@k (Rk) and nDCG@k (Nk). Results are reported as percentages. Best scores are bolded, second-best underlined. ID stands for ID-based, T stands for Text-based. 

|**Model**||**Beauty**|**Beauty**|||**Games**|**Games**|||**Baby**|**Baby**||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||R10|N10|R50|N50|R10|N10|R50|N50|R10|N10|R50|N50|
|**GRU4RecID**|0.31|0.15|1.11|0.32|2.11|1.14|5.28|1.82|1.10|0.56|3.55|1.09|
|**SASRecID**|0.31|0.18|0.84|0.30|2.32|1.15|5.55|1.85|1.23|0.58|3.69|1.11|
|**GRU4RecT**|||||||||||||
|BL!IRB|0.63|0.30|1.67|0.53|2.16|1.14|5.43|1.84|1.29|0.65|4.05|1.24|
|BL!IRL|0.84|0.42|2.09|0.69|2.35|1.29|5.90|2.06|1.26|0.64|3.96|1.22|
|t-emb-3|0.57|0.27|1.78|0.55|3.01|1.64|7.39|2.59|0.44|0.21|1.67|0.47|
|NVEmb†|0.75|0.36|1.74|0.57|2.98_𝐿_1.65_𝐿_<br>7.27_𝐿_2.57_𝐿_1.63<br>_𝐿_0.84<br>_𝐿_**4.92**_𝐿_1.54<br>_𝐿_||||||||
|KALM|0.69|0.36|1.76|0.59|2.67|1.46|6.52|2.30|1.45|0.73|4.51|1.38|
|**SASRecT**|||||||||||||
|BL!IRB|0.69|0.35|2.16|0.66|1.90|1.01|5.01|1.68|1.24|0.63|3.84|1.19|
|BL!IRL|1.21|0.50|2.55_𝐿_0.77||2.18|1.17|5.36|1.86|1.33|0.68|4.04|1.26|
|t-emb-3|0.84|0.42|2.20|0.71|2.77|1.51|6.92|2.41|0.40|0.20|1.43|0.42|
|NVEmb†|0.77|0.43|2.05|0.70|2.78_𝐿_1.54_𝐿_6.87_𝐿_2.42_𝐿_1.50_𝐿_0.75_𝐿_4.51_𝐿_1.40_𝐿_||||||||
|KALM|0.88|0.45|1.80|0.65|2.40|1.30|5.83|2.04|1.44|0.73|4.38|1.35|
|**UniSRecT**|||||||||||||
|BL!IRB|2.60|1.39|4.69|1.85|2.47|1.30|6.08|2.07|1.52|0.77|4.34|1.37|
|BL!IRL|2.51|1.38|4.54|1.83|2.53|1.37|6.24|2.17|1.53|0.78|4.36|1.39|
|t-emb-3|**3.60**_𝐿_**1.86**_𝐿_**5.73**_𝐿_**2.31**_𝐿_3.05|||||1.64|7.46|2.59|0.44|0.24|1.57|0.48|
|NVEmb†|2.93|1.58|4.77|2.00|**3.11**_𝐿_**1.65**_𝐿_**7.50**_𝐿_**2.59**_𝐿_**1.72**_𝐿_**0.89**_𝐿_4.87_𝐿_<br>**1.57**_𝐿_||||||||
|KALM|3.45|1.84|5.55|2.29|2.75|1.47|6.68|2.32|1.55|0.78|4.39|1.39|



([†] ) NVEmb is adopted as abbreviation of NVEmbed-v2. 

( _[𝐿]_ ) Statistically signi!cant improvement (p < 0.001) between the best GTE model and the best BL!IR-based model. 

strategy proposed by Hou et al. [10], using item descriptions as textual inputs. This results in two variants for each model: an **ID** -based version using standard embeddings and a **T** ext-based version with text-derived representations. For the text-based variants, we test several pre-trained text embedding models: BL!IR [10] (base and large), OpenAI’s text-embedding-3-large[2] (t-emb-3) and two open-source GTEs: KALM [25] and NVEmbed-v2 [17]. KALM matches BL!IR in parameter count and embedding size for fair comparison, while NVEmbed-v2 o"ers a more powerful GTE with higher dimensionality and a larger parameter footprint. 

For PS, we expand our evaluation to include a range of text encoders: RoBERTaBASE [20], ColBERTv2 [31], mGTE [39], I"#$%&’$ORXL [32], Sentence-T5XXL [25], Jasper [37], and GTE-Qwen2 [19]. These models represent a mix of encoderand decoder-based transformers, covering various parameter sizes and embedding dimensions for a comprehensive comparison. 

_4.1.3 Evaluation Protocol._ For SR, we employ the RecBole [40, 41] framework, adopting the optimized hyperparameter settings from [10], as they are already well-tuned for the Amazon Reviews 2023 dataset and ensure fair comparison. Early stopping is applied based on nDCG@10 with a patience of 10. For PS, models are implemented using Hugging Face Transformers, with a maximum input sequence length of 512. Retrieval is performed using cosine similarity, which empirically outperforms Euclidean and dot product measures. The metrics employed are Recall and nDCG. We analyze embedding space utilization by computing the _𝑈_ -e"ective dimension using PCA on a random sample of 100,000 item embeddings [30]. 

Attimonelli et al. 

6 

Table 2. Comparison of text encoders for product search (nDCG@100) on the two datasets (results are percentages). “All” averages scores for all domains. We also report two domains, “O!ice” and “Sports”. 

|**Model**<br>**#Par**<br>**#Dim**|**ESCI**|**Amazon-C4**|
|---|---|---|
||**All**<br>O#ce Sports|**All**<br>O#ce Sports|
|**BM25**<br>—<br>—|1.10<br>1.35<br>1.57|0.00<br>0.00<br>0.00|
|_Encoders_<br>**RoBERTa**B<br>123M<br>768<br>**ColBERTv2**<br>110M<br>768<br>**BL!IR**B<br>123M<br>768<br>**BL!IR**L<br>354M 1024 <br>**mGTE**<br>305M<br>768<br>**I"#$%&’$OR**XL<br>1.5B<br>768<br>**Sentence-T5**XXL<br>11B<br>768|0.08<br>0.03<br>0.25<br>1.71<br>1.80<br>1.44<br>11.76<br>12.56<br>14.26<br> 12.12<br>12.81<br>13.89<br>22.17<br>22.32<br>24.12<br>20.53<br>20.13<br>21.32<br>21.75<br>22.13<br>22.98|0.25<br>0.33<br>0.37<br>0.88<br>1.60<br>0.51<br>14.90<br>18.02<br>22.24<br>17.18<br>20.07<br>25.68<br>13.11<br>15.33<br>17.38<br>12.22<br>15.79<br>16.38<br>13.88<br>17.77<br>19.22|
|_Decoders_<br>**KALM**<br>0.5B<br>896<br>**Jasper**<br>2B<br>1024 <br>**GTE-Qwen2**<br>7B<br>3584 <br>**NVEmbed-v2**<br>11B<br>4096|23.12<br>23.76<br>24.39<br>15.61<br>18.55<br>22.01<br> 26.62<br>26.07<br>27.11<br>17.10<br>20.23<br>23.16<br> **28.06**_𝐿_**28.09**_𝐿_**29.09**_𝐿_17.92<br>**21.41**_𝐿_24.03<br> 27.59<br>27.24<br>28.45<br>**19.02**_𝐿_21.32<br>**25.91**_𝐿_||
|**t-emb-3**<br>—<br>3072|25.76<br>24.67<br>26.96<br>17.53<br>20.86<br>25.23||



( _[𝐿]_ ) Statistically signi!cant improvement (p < 0.001) between the best GTE model and the best BL!IR-based model. 

## **4.2 Model Comparison (RQ1)** 

Table 1 presents the results for the SR task. Textual embeddings consistently outperform ID-based models, highlighting the importance of semantic item information. Among the embedding models, NVEmbed-v2 and KALM, both of the GTE family, deliver the most substantial gains across all architectures. NVEmbed-v2 achieves the best results on the Games and Baby categories, while KALM slightly outperforms NVEmbed-v2 on Beauty. Such improvements o"ered by leading GTE models are statistically signi!cant compared to the best BL!IR baseline for most text-based architectures and datasets. The signi!cance was evaluated by comparing the best GTE with the leading BL!IR variant for each model-dataset pair, based on nDCG@10. Furthermore, GTEs surpass the closed-source model t-emb-3 on two datasets. These results showcase the bene!ts of recent, high-capacity embedding methods that do not depend on domain-speci!c knowledge. 

Table 2 shows the PS results on the ESCI and Amazon-C4 datasets. GTE-based models consistently surpass traditional models (RoBERTa and ColBERTv2) and BL!IR. Notably, top-performing GTEs achieve statistically signi!cant gains over the best-performing BL!IR baseline, validating the superiority of the GTE approach. Scores are generally higher on ESCI due to its simpler queries: GTE-Qwen2 improves from 0.1792 on Amazon-C4 to 0.2806 on ESCI, and Jasper from 0.1710 to 0.2662. An exception is BL!IR, which performs well on Amazon-C4 but drops sharply on ESCI, suggesting that !ne-tuning hinders generalization. RoBERTa performs worse across the board, re$ecting its limitations in retrieval tasks. Among the top performers are high-capacity GTEs, with NVEmbed-v2 leading on Amazon-C4 and GTE-Qwen2 on ESCI. 

Overall, our !ndings indicate that **GTEs achieve strong performance in both tasks without requiring taskspeci!c !ne-tuning, outperforming traditional and !ne-tuned solutions, as well as closed-source models** . 

## **4.3 Model Analysis (RQ2)** 

To understand the superior performance of GTEs, we analyze model capacity, embedding structure, and architectural design. Table 2 shows that **performance does not scale linearly with model capacity** (no. of parameters) **and** 

2API version: 2024-02-01 

Do We Really Need Specialization? Evaluating GTEs for Zero-Shot Recommendation and Search 

7 

**==> picture [398 x 163] intentionally omitted <==**

**----- Start of picture text -----**<br>
BL!IRB BL!IRL mGTE I"#$%&’$ORXL<br>Sentence-T5XXL KALM Jasper GTE-Qwen2<br>NVEmbed-v2 text-emb-3<br>0 . 3<br>0 . 25<br>0 . 2<br>0 . 15<br>0 . 1<br>10 [2] 10 [3] 10 [2] 10 [3]<br># of components in log-scale # of components in log-scale<br>(a) ESCI (b) Amazon-C4<br>nDCG<br>**----- End of picture text -----**<br>


Fig. 1. nDCG scores for various models on the two PS datasets (a) ESCI and (b) Amazon-C4 versus the number of components (log-scale). Points shown correspond to component counts yielding 80%, 95%, and 100% explained variance. 

**dimensionality** : KALM (0.5B) outperforms larger models such as I"#$%&’$ORXL (1.5B) and Sentence-T5XXL (11B), while Jasper (1024 dimensions) outperforms t-emb-3 (3072 dimensions) on ESCI. In the SR task, KALM is found to outperform high-dimensional GTEs under speci!c model-dataset combinations (e.g., GRU4Rec-Beauty). 

To assess space utilization, we compute the _𝑈_ -e"ective-dimensionality (Section 3.2). Figure 1 shows how nDCG varies with the number of retained components in the PS task (points correspond to _𝑈_ values of 0.80, 0.95, and 1.00, left to right). An nDCG increase with fewer components suggests noisy directions in the feature space, while a drop indicates that information is uniformly distributed. We observe that for large GTEs (e.g., NVEmbed-v2 and GTE-Qwen2), the number of dimensions needed to preserve 80% of the total variance is close to the full dimensionality of BL!IRB, suggesting more e#cient use of representational space. BL!IR exhibits a signi!cant drop in components with _𝑈_ = 0 _._ 80, hinting at high anisotropy [4]. For GTEs, this phenomenon is less pronounced. While BL!IR bene!ts from PCA showing a marked inverted-U trend, many GTEs show a plateau or slight improvement at 95% variance: for large GTEs, moderate compression substantially reduces dimensionality without compromising performance. Conversely, on Amazon-C4, all models bene!t from compression, resulting in a performance gain. This trend is particularly pronounced for BL!IR, indicating presence of noise in low-variance components. 

Architecturally, we note that decoder-style models (Jasper, GTE-Qwen2, NVEmbed-v2) outperform encoder-based ones, with generative, autoregressive, or retrieval-oriented training yielding semantically rich, task-aligned representations [1, 17]. 

Overall, we show that **GTEs, particularly decoder-based ones, tend to spread useful information more evenly across embedding dimensions** , possibly explaining their strong performance. In contrast, we !nd that **model capacity and dimensionality often show little correlation with downstream performance** . 

## **5 Conclusion and Future Work** 

This work investigates the zero-shot capabilities of GTEs in sequential recommendation and product search. Despite the potential advantages of domain-speci!c !ne-tuning, we !nd that GTEs can outperform !ne-tuned models (e.g., BL!IR), classical architectures (e.g., ColBERT), and closed-source solutions (e.g., OpenAI) without task-speci!c adaptation. We 

Attimonelli et al. 

8 

identify more uniform space utilization as a key factor for their success and show that emphasizing the most informative dimensions via PCA can boost the performance of !ne-tuned models and e"ectively compress dimensionality for large GTEs. These results position GTEs as strong alternatives when !ne-tuning is impractical. Future work may further enhance embedding properties such as isotropy and disentanglement, also explored in state-of-the-art models such as UniSRec. 

## **References** 

- [1] Parishad BehnamGhader, Vaibhav Adlakha, Marius Mosbach, Dzmitry Bahdanau, Nicolas Chapados, and Siva Reddy. 2024. LLM2Vec: Large Language Models Are Secretly Powerful Text Encoders. _CoRR_ abs/2404.05961 (2024). 

- [2] OpenAI Blog. 2022. Introducing ChatGPT. https://openai.com/index/chatgpt/. [Accessed 18-04-2025]. 

- [3] Artun Boz, Wouter Zorgdrager, Zoe Kotti, Jesse Harte, Panos Louridas, Dietmar Jannach, and Marios Fragkoulis. 2024. Improving Sequential Recommendations with LLMs. _CoRR_ abs/2402.01339 (2024). doi:10.48550/ARXIV.2402.01339 arXiv:2402.01339 

- [4] Xingyu Cai, Jiaji Huang, Yuchen Bian, and Kenneth Church. 2021. Isotropy in the Contextual Embedding Space: Clusters and Manifolds. In _ICLR_ . OpenReview.net. 

- [5] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. In _NAACL-HLT (1)_ . Association for Computational Linguistics, 4171–4186. 

- [6] Kawin Ethayarajh. 2019. How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings. In _EMNLP/IJCNLP (1)_ . Association for Computational Linguistics, 55–65. 

- [7] Tianyu Gao, Xingcheng Yao, and Danqi Chen. 2021. SimCSE: Simple Contrastive Learning of Sentence Embeddings. In _EMNLP (1)_ . Association for Computational Linguistics, 6894–6910. 

- [8] Jesse Harte, Wouter Zorgdrager, Panos Louridas, Asterios Katsifodimos, Dietmar Jannach, and Marios Fragkoulis. 2023. Leveraging Large Language Models for Sequential Recommendation. In _Proceedings of the 17th ACM Conference on Recommender Systems, RecSys 2023, Singapore, Singapore, September 18-22, 2023_ , Jie Zhang, Li Chen, Shlomo Berkovsky, Min Zhang, Tommaso Di Noia, Justin Basilico, Luiz Pizzato, and Yang Song (Eds.). ACM, 1096–1102. doi:10.1145/3604915.3610639 

- [9] Balázs Hidasi, Alexandros Karatzoglou, Linas Baltrunas, and Domonkos Tikk. 2016. Session-based Recommendations with Recurrent Neural Networks. In _ICLR (Poster)_ . 

- [10] Yupeng Hou, Jiacheng Li, Zhankui He, An Yan, Xiusi Chen, and Julian J. McAuley. 2024. Bridging Language and Items for Retrieval and Recommendation. _CoRR_ abs/2403.03952 (2024). 

- [11] Yupeng Hou, Shanlei Mu, Wayne Xin Zhao, Yaliang Li, Bolin Ding, and Ji-Rong Wen. 2022. Towards Universal Sequence Representation Learning for Recommender Systems. In _KDD_ . ACM, 585–593. 

- [12] Xinshuo Hu, Zifei Shan, Xinping Zhao, Zetian Sun, Zhenyu Liu, Dongfang Li, Shaolin Ye, Xinyuan Wei, Qian Chen, Baotian Hu, Haofen Wang, Jun Yu, and Min Zhang. 2025. KaLM-Embedding: Superior Training Data Brings A Stronger Embedding Model. _CoRR_ abs/2501.01028 (2025). doi:10.48550/ARXIV.2501.01028 arXiv:2501.01028 

- [13] Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de Las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed. 2023. Mistral 7B. _CoRR_ abs/2310.06825 (2023). 

- [14] Wang-Cheng Kang and Julian J. McAuley. 2018. Self-Attentive Sequential Recommendation. In _ICDM_ . IEEE Computer Society, 197–206. 

- [15] Omar Khattab and Matei Zaharia. 2020. ColBERT: E#cient and E"ective Passage Search via Contextualized Late Interaction over BERT. In _SIGIR_ . ACM, 39–48. 

- [16] Aditya Kusupati, Gantavya Bhatt, Aniket Rege, Matthew Wallingford, Aditya Sinha, Vivek Ramanujan, William Howard-Snyder, Kaifeng Chen, Sham M. Kakade, Prateek Jain, and Ali Farhadi. 2022. Matryoshka Representation Learning. In _NeurIPS_ . 

- [17] Chankyu Lee, Rajarshi Roy, Mengyao Xu, Jonathan Raiman, Mohammad Shoeybi, Bryan Catanzaro, and Wei Ping. 2024. NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models. _CoRR_ abs/2405.17428 (2024). 

- [18] Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang, Yiming Yang, and Lei Li. 2020. On the Sentence Embeddings from Pre-trained Language Models. In _EMNLP (1)_ . Association for Computational Linguistics, 9119–9130. 

- [19] Zehan Li, Xin Zhang, Yanzhao Zhang, Dingkun Long, Pengjun Xie, and Meishan Zhang. 2023. Towards General Text Embeddings with Multi-stage Contrastive Learning. _CoRR_ abs/2308.03281 (2023). doi:10.48550/ARXIV.2308.03281 arXiv:2308.03281 

- [20] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019. RoBERTa: A Robustly Optimized BERT Pretraining Approach. _CoRR_ abs/1907.11692 (2019). 

- [21] Anemily Machina and Robert E. Mercer. 2024. Anisotropy is Not Inherent to Transformers. In _NAACL-HLT_ . Association for Computational Linguistics, 4892–4907. 

- [22] Simone Merlo, Guglielmo Faggioli, and Nicola Ferro. 2025. A Reproducibility Study for Joint Information Retrieval and Recommendation in Product Search. In _Advances in Information Retrieval_ . Springer Nature Switzerland, Cham, 130–145. 

Do We Really Need Specialization? Evaluating GTEs for Zero-Shot Recommendation and Search 9 

- [23] Felice Antonio Merra, Omar Zaidan, and Fabricio de Sousa Nascimento. 2023. Improving the Relevance of Product Search for Queries with Negations. In _WWW (Companion Volume)_ . ACM, 86–89. 

- [24] Niklas Muennigho", Nouamane Tazi, Loïc Magne, and Nils Reimers. 2023. MTEB: Massive Text Embedding Benchmark. In _EACL_ . Association for Computational Linguistics, 2006–2029. 

- [25] Jianmo Ni, Gustavo Hernández Ábrego, Noah Constant, Ji Ma, Keith B. Hall, Daniel Cer, and Yinfei Yang. 2022. Sentence-T5: Scalable Sentence Encoders from Pre-trained Text-to-Text Models. In _ACL (Findings)_ . Association for Computational Linguistics, 1864–1874. 

- [26] Jianmo Ni, Chen Qu, Jing Lu, Zhuyun Dai, Gustavo Hernández Ábrego, Ji Ma, Vincent Y. Zhao, Yi Luan, Keith B. Hall, Ming-Wei Chang, and Yinfei Yang. 2022. Large Dual Encoders Are Generalizable Retrievers. In _EMNLP_ . Association for Computational Linguistics, 9844–9855. 

- [27] Jacob P. Portes, Alexander Trott, Sam Havens, Daniel King, Abhinav Venigalla, Moin Nadeem, Nikhil Sardana, Daya Khudia, and Jonathan Frankle. 2023. MosaicBERT: A Bidirectional Encoder Optimized for Fast Pretraining. In _NeurIPS_ . 

- [28] Colin Ra"el, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. 2020. Exploring the Limits of Transfer Learning with a Uni!ed Text-to-Text Transformer. _J. Mach. Learn. Res._ 21 (2020), 140:1–140:67. 

- [29] Chandan K. Reddy, Lluís Màrquez, Fran Valero, Nikhil Rao, Hugo Zaragoza, Sambaran Bandyopadhyay, Arnab Biswas, Anlu Xing, and Karthik Subbian. 2022. Shopping Queries Dataset: A Large-Scale ESCI Benchmark for Improving Product Search. _CoRR_ abs/2206.06588 (2022). 

- [30] William Rudman, Nate Gillman, Taylor Rayne, and Carsten Eickho". 2022. IsoScore: Measuring the Uniformity of Embedding Space Utilization. In _ACL (Findings)_ . Association for Computational Linguistics, 3325–3339. 

- [31] Keshav Santhanam, Omar Khattab, Jon Saad-Falcon, Christopher Potts, and Matei Zaharia. 2022. ColBERTv2: E"ective and E#cient Retrieval via Lightweight Late Interaction. In _NAACL-HLT_ . Association for Computational Linguistics, 3715–3734. 

- [32] Hongjin Su, Weijia Shi, Jungo Kasai, Yizhong Wang, Yushi Hu, Mari Ostendorf, Wen-tau Yih, Noah A. Smith, Luke Zettlemoyer, and Tao Yu. 2023. One Embedder, Any Task: Instruction-Finetuned Text Embeddings. In _ACL (Findings)_ . Association for Computational Linguistics, 1102–1121. 

- [33] Jianlin Su, Murtadha H. M. Ahmed, Yu Lu, Shengfeng Pan, Wen Bo, and Yunfeng Liu. 2024. RoFormer: Enhanced transformer with Rotary Position Embedding. _Neurocomputing_ 568 (2024), 127063. 

- [34] Fei Sun, Jun Liu, Jian Wu, Changhua Pei, Xiao Lin, Wenwu Ou, and Peng Jiang. 2019. BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer. In _CIKM_ . ACM, 1441–1450. 

- [35] An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, Guanting Dong, Haoran Wei, Huan Lin, Jialong Tang, Jialin Wang, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Ma, Jianxin Yang, Jin Xu, Jingren Zhou, Jinze Bai, Jinzheng He, Junyang Lin, Kai Dang, Keming Lu, Keqin Chen, Kexin Yang, Mei Li, Mingfeng Xue, Na Ni, Pei Zhang, Peng Wang, Ru Peng, Rui Men, Ruize Gao, Runji Lin, Shijie Wang, Shuai Bai, Sinan Tan, Tianhang Zhu, Tianhao Li, Tianyu Liu, Wenbin Ge, Xiaodong Deng, Xiaohuan Zhou, Xingzhang Ren, Xinyu Zhang, Xipin Wei, Xuancheng Ren, Xuejing Liu, Yang Fan, Yang Yao, Yichang Zhang, Yu Wan, Yunfei Chu, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, Zhifang Guo, and Zhihao Fan. 2024. Qwen2 Technical Report. _CoRR_ abs/2407.10671 (2024). 

- [36] Zheng Yuan, Fajie Yuan, Yu Song, Youhua Li, Junchen Fu, Fei Yang, Yunzhu Pan, and Yongxin Ni. 2023. Where to Go Next for Recommender Systems? ID- vs. Modality-based Recommender Models Revisited. In _SIGIR_ . ACM, 2639–2649. 

- [37] Dun Zhang and FulongWang. 2024. Jasper and Stella: distillation of SOTA embedding models. _CoRR_ abs/2412.19048 (2024). 

- [38] Lingzi Zhang, Xin Zhou, Zhiwei Zeng, and Zhiqi Shen. 2024. Dual-View Whitening on Pre-trained Text Embeddings for Sequential Recommendation. In _AAAI_ . AAAI Press, 9332–9340. 

- [39] Xin Zhang, Yanzhao Zhang, Dingkun Long, Wen Xie, Ziqi Dai, Jialong Tang, Huan Lin, Baosong Yang, Pengjun Xie, Fei Huang, Meishan Zhang, Wenjie Li, and Min Zhang. 2024. mGTE: Generalized Long-Context Text Representation and Reranking Models for Multilingual Text Retrieval. In _EMNLP (Industry Track)_ . Association for Computational Linguistics, 1393–1412. 

- [40] Wayne Xin Zhao, Yupeng Hou, Xingyu Pan, Chen Yang, Zeyu Zhang, Zihan Lin, Jingsen Zhang, Shuqing Bian, Jiakai Tang, Wenqi Sun, Yushuo Chen, Lanling Xu, Gaowei Zhang, Zhen Tian, Changxin Tian, Shanlei Mu, Xinyan Fan, Xu Chen, and Ji-Rong Wen. 2022. RecBole 2.0: Towards a More Up-to-Date Recommendation Library. In _CIKM_ . ACM, 4722–4726. 

- [41] Wayne Xin Zhao, Shanlei Mu, Yupeng Hou, Zihan Lin, Yushuo Chen, Xingyu Pan, Kaiyuan Li, Yujie Lu, Hui Wang, Changxin Tian, Yingqian Min, Zhichao Feng, Xinyan Fan, Xu Chen, Pengfei Wang, Wendi Ji, Yaliang Li, Xiaoling Wang, and Ji-Rong Wen. 2021. RecBole: Towards a Uni!ed, Comprehensive and E#cient Framework for Recommendation Algorithms. In _CIKM_ . ACM, 4653–4664. 

