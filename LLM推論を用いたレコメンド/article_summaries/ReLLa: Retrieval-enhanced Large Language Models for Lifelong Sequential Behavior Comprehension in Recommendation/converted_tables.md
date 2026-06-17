### Table 1: The dataset statistics.

| Dataset | \#Users | \#Items | \#Samples | \#Fields | \#Features |
| --- | --- | --- | --- | --- | --- |
| BookCrossing | 278,858 | 271,375 | 17,714 | 10 | 912,279 |
| MovieLens-1M | 6,040 | 3,706 | 970,009 | 10 | 16,944 |
| MovieLens-25M | 162,541 | 59,047 | 25,000,095 | 6 | 280,576 \\ \bottomrule |

### Table 2: The performance of different models in \emph{zero-shot

| Model | BookCrossing | MovieLens-1M | MovieLens-25M |
| --- | --- | --- | --- |
|  | AUC | Log Loss | ACC | Rel.Impr | AUC | Log Loss | ACC | Rel.Impr | AUC | Log Loss | ACC | Rel.Impr |
| Zero-shot | Vicuna-7B | 0.7011 | <u>0.9357</u> | 0.5378 | 3.45\% | 0.6739 | 0.9510 | 0.5644 | 4.07\% | <u>0.7468</u> | 0.6348 | 0.6392 | -1.93\% |
|  | Vicuna-13B | <u>0.7176</u> | 0.9507 | <u>0.5649</u> | 1.07\% | 0.6993 | 0.6291 | 0.6493 | 0.29\% | **0.7503** | <u>0.6308</u> | <u>0.6427</u> | -2.39\% |
|  | ReLLa (Ours) | **0.7253$^*$** | **0.9277$^*$** | **0.5750$^*$** | - | **0.7013$^*$** | **0.6250$^*$** | **0.6507$^*$** | - | 0.7324 | **0.5858$^*$** | **0.7027$^*$** | - |
| Full-shot | DeepFM | 0.7496 | 0.5953 | 0.6760 | 1.05\% | 0.7915 | 0.5484 | 0.7225 | 1.49\% | 0.8189 | 0.4867 | 0.7709 | 3.52\% |
|  | AutoInt | 0.7481 | 0.6840 | 0.6365 | 1.26\% | 0.7929 | 0.5453 | 0.7226 | 1.31\% | 0.8169 | 0.4957 | 0.7689 | 3.77\% |
|  | DCNv2 | 0.7472 | 0.6816 | 0.6472 | 1.38\% | 0.7931 | 0.5464 | 0.7216 | 1.29\% | 0.8190 | 0.4989 | 0.7702 | 3.50\% |
|  | GRU4Rec | 0.7479 | 0.5930 | 0.6777 | 1.28\% | 0.7926 | 0.5453 | 0.7225 | 1.35\% | 0.8186 | 0.4941 | 0.7700 | 3.55\% |
|  | Caser | 0.7478 | 0.5990 | 0.6760 | 1.30\% | 0.7918 | 0.5464 | 0.7206 | 1.45\% | 0.8199 | 0.4865 | 0.7707 | 3.39\% |
|  | SASRec | 0.7482 | 0.5934 | **0.6811** | 1.24\% | 0.7934 | 0.5460 | 0.7233 | 1.25\% | 0.8187 | 0.4956 | 0.7691 | 3.54\% |
|  | DIN | 0.7477 | 0.6811 | 0.6557 | 1.31\% | 0.7962 | 0.5425 | 0.7252 | 0.89\% | 0.8190 | 0.4906 | 0.7716 | 3.50\% |
|  | SIM | <u>0.7541</u> | **0.5893** | 0.6777 | 0.45\% | <u>0.7992</u> | <u>0.5387</u> | <u>0.7268</u> | 0.51\% | <u>0.8344</u> | <u>0.4724</u> | <u>0.7822</u> | 1.59\% |
|  | CTR-BERT | 0.7448 | 0.5938 | 0.6704 | 1.71\% | 0.7931 | 0.5457 | 0.7233 | 1.29\% | 0.8079 | 0.5044 | 0.7511 | 4.93\% |
|  | PTab | 0.7429 | 0.6154 | 0.6574 | 1.97\% | 0.7955 | 0.5428 | 0.7240 | 0.98\% | 0.8107 | 0.5022 | 0.7551 | 4.56\% |
|  | P5 | 0.7438 | 0.6128 | 0.6563 | 1.84\% | 0.7937 | 0.5478 | 0.7190 | 1.21\% | 0.8092 | 0.5030 | 0.7527 | 4.76\% |
| Few-shot | ReLLa (<1\%) | 0.7482 | 0.6265 | 0.6800 | - | 0.7927 | 0.5475 | 0.7196 | - | 0.8352 | 0.4693 | 0.7779 | - |
|  | ReLLa (<10\%) | **0.7575$^*$** | <u>0.5919</u> | <u>0.6806</u> | - | **0.8033$^*$** | **0.5362$^*$** | **0.7280$^*$** | - | **0.8477$^*$** | **0.4524$^*$** | **0.7925$^*$** | - |

### Table 3: The performance of different models in \emph{zero-shot



### Table 4: The performance of different variants of ReLLa. We remove different components of ReLLa to evaluate the contribution of each part to the model. The best result is given in bold, and the second-best value is underlined.

| Model Variant | BookCrossing | MovieLens-1M | MovieLens-25M |
| --- | --- | --- | --- |
|  | AUC | Log Loss | ACC | AUC | Log Loss | ACC | AUC | Log Loss | ACC |
| ReLLa (Ours) | **0.7482** | <u>0.6265</u> | **0.6800** | **0.7927** | **0.5475** | **0.7196** | **0.8352** | **0.4693** | **0.7779** |
| ReLLa (w/o Mixture) | 0.7399 | **0.6002** | 0.6715 | 0.7849 | <u>0.5693</u> | 0.6985 | 0.8192 | 0.4904 | <u>0.7715</u> |
| ReLLa (w/o Retrieval) | 0.7167 | 0.9293 | 0.4898 | 0.7718 | 0.5795 | <u>0.7039</u> | 0.8174 | <u>0.4892</u> | 0.7685 |
| ReLLa ($\frac{1}{2}N$-shot) | <u>0.7415</u> | 0.6268 | 0.6462 | <u>0.7862</u> | 0.5781 | 0.6964 | <u>0.8231</u> | 0.5157 | 0.7672 |
| ReLLa (w/o IT) | 0.7253 | 0.9277 | 0.5750 | 0.7013 | 0.6250 | 0.6507 | 0.7324 | 0.5858 | 0.7027 |
| ReLLa (w/o IT \ | Retrieval) | 0.7176 | 0.9507 | 0.5649 | 0.6993 | 0.6291 | 0.6493 | 0.7503 | 0.6308 | 0.6427 |

### Table 5: Zero-shot AUC performance w.r.t. different sequence length $K$ for different LLMs on MovieLens-1M dataset. The peaking performance for each LLM is given in bold.

| LLM | MovieLens-1M |
| --- | --- |
|  | K=5 | K=10 | K=15 | K=20 | K=25 | K=30 |
| Falcon-7B | **0.5906** | 0.5741 | 0.5583 | 0.5420 | 0.5468 | 0.5452 |
| Mistral-7B | 0.6566 | 0.6568 | **0.6670** | 0.6623 | 0.6612 | 0.6610 |
| Vicuna-7B | 0.6630 | 0.6586 | **0.6739** | 0.6527 | 0.6463 | 0.6412 |
| Vicuna-13B | 0.6807 | 0.6932 | **0.6993** | 0.6918 | 0.6937 | 0.6908 |
| LLaMA2-70B | 0.6259 | 0.6348 | **0.6421** | 0.6402 | 0.6339 | 0.6321 |

### Table 6: The model compatibility of ReLLa w.r.t. different backbone LLMs on MovieLens-1M dataset with $K$=30. We also give the performance of SIM, which is the best baseline among traditional recommendation models.

| Model | MovieLens-1M |
| --- | --- |
|  | AUC | Log Loss | ACC |
| SIM | few-shot (<1\%) | 0.7352 | 0.6132 | 0.6743 |
|  | few-shot (<10\%) | 0.7414 | 0.6129 | 0.6756 |
|  | full-shot | **0.7992** | **0.5387** | **0.7268** |
| Falcon-7B | zero-shot | 0.5906 | 0.7674 | 0.5436 |
|  | with SUBR | 0.5964 | 0.7709 | 0.5437 |
|  | with ReiT (<1\%) | 0.7811 | 0.5589 | 0.7111 |
|  | with ReiT (<10\%) | **0.7870** | **0.5658** | **0.7072** |
| Mistral-7B | zero-shot | 0.6670 | 0.7556 | 0.4793 |
|  | with SUBR | 0.6881 | 0.7321 | 0.5119 |
|  | with ReiT (<1\%) | 0.7905 | 0.5488 | 0.7210 |
|  | with ReiT (<10\%) | **0.8005** | **0.5388** | **0.7275** |
| Vicuna-7B | zero-shot | 0.6739 | 0.9510 | 0.5644 |
|  | with SUBR | 0.6704 | 0.7745 | 0.5655 |
|  | with ReiT (<1\%) | 0.7918 | 0.5493 | 0.7196 |
|  | with ReiT (<10\%) | **0.8016** | **0.5365** | **0.7274** |
| Vicuna-13B | zero-shot | 0.6993 | 0.6291 | 0.6493 |
|  | with SUBR | 0.7013 | 0.6250 | 0.6507 |
|  | with ReiT (<1\%) | 0.7927 | 0.5475 | 0.7196 |
|  | with ReiT (<10\%) | **0.8033** | **0.5362** | **0.7280** |

### Table 7: Complexity analysis on MovieLens-1M dataset.

| Model | \# Total Parameter | \# Trainable Parameter | Inference Time |
| --- | --- | --- | --- |
| SIM | 1.44M | 1.44M | 3.21ms |
| ReLLa | 13B | 650M | 500ms |

### Table 8: Ablation study w.r.t different PCA dimensionalities for ReLLa on MovieLens-1M dataset under both zero-shot and few-shot (<1\%) settings.

| Setting | PCA Dim. | MovieLens-1M |
| --- | --- | --- |
|  |  | AUC | Log Loss | ACC |
| zero-shot | 512 | 0.7013 | **0.6250** | **0.6507** |
|  | 256 | **0.7064** | 0.6377 | 0.6357 |
|  | 128 | 0.7063 | 0.6379 | 0.6351 |
|  | 64 | 0.7057 | 0.6375 | 0.6349 |
| few-shot | 512 | **0.7927** | **0.5475** | **0.7196** |
|  | 256 | 0.7917 | 0.5476 | 0.7098 |
|  | 128 | 0.7897 | 0.5606 | 0.7099 |
|  | 64 | 0.7901 | 0.5629 | 0.7099 |

### Table 9: Ablation study w.r.t different distance metrics for ReLLa on MovieLens-1M dataset under both zero-shot and few-shot (<1\%) settings.

| Setting | Distance | MovieLens-1M |
| --- | --- | --- |
|  |  | AUC | Log Loss | ACC |
| zero-shot | Cosine | **0.7013** | **0.6250** | **0.6507** |
|  | L2 | 0.6975 | 0.6356 | 0.6386 |
|  | L1 | 0.6811 | 0.6388 | 0.6339 |
| Few-shot | Cosine | **0.7927** | **0.5475** | **0.7196** |
|  | L2 | 0.7872 | 0.5762 | 0.6944 |
|  | L1 | 0.7833 | 0.5598 | 0.7119 |

### Table 10: The averaged heterogeneity scores of two sequence types w.r.t. different length $K$.

| Seq. Type | MovieLens-1M |
| --- | --- |
|  | K=5 | K=10 | K=15 | K=20 | K=25 | K=30 |
| Top Recent (Origin) | 2.91 | 4.19 | 5.09 | 5.80 | 6.39 | 6.90 |
| Top Relevant (Retrieval) | 2.44 | 3.37 | 4.01 | 4.51 | 4.94 | 5.32 |
