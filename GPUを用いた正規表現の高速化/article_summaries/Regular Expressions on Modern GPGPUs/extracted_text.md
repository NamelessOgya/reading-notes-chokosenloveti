## **Regular Expressions on Modern GPGPUs** 

Cheng Li cheng.li2@mail.mcgill.ca McGill University Montréal, Québec, Canada 

## **ABSTRACT** 

Using GPUs is an effective way to accelerate regular expression (RE) matching, offering orders of magnitude faster processing than pure CPU approaches. Prior GPU-based RE acceleration methods, however, were developed on older GPU models and primarily aimed at expediting network packet inspection problems. In this work we conduct an updated study aiming to improve performance and enhance generality. We first incorporate prefiltering, verifying whether simpler parts of the RE can match before testing more complex RE components. We also observed that naive implementation of current designs on a modern GPU results in low thread occupancy, limiting performance, and improving the selection of GPU parameters is also crucial to optimizing performance. In combination our optimized design allows us to achieve 40x performance improvement over iNFAnt [5] and up to 1900x faster than ASyncAP [11]. Such an updated approach allows for faster, more general RE matching on modern GPUs. 

Clark Verbrugge clump@cs.mcgill.ca McGill University Montréal, Québec, Canada 

In this work, we present an updated approach. By incorporating a simple prefiltering technique we are able to test more complex REs without major degradation. This gives us an adaptive approach with applicability to a wider range of REs. We also explore performance in terms of GPU resource usage. Adjustments to register allocation, block size, and memory use further improve performance, better saturating the GPU. Experimental analysis using Snort’s RE dataset show an impressive performance improvement, around 40x that of iNFAnt [5] and as much as 1900x faster than ASyncAP [11] on a consumer-grade GPU. Our results demonstrate that although conceptually simple, close attention to RE structure as well as to how the implementation synergizes with GPU resources can result in multiple orders of magnitude improvement. 

In the section that follows we briefly describe related work on implementing RE matching on GPUs. Section 3 describes our prefiltering design, while section 4 describes our approach to improving thread occupancy. We give experimental data in section 5 prior to concluding. 

## **KEYWORDS** 

GPU, Cuda, regular expressions, pattern-matching 

## **ACM Reference Format:** 

Cheng Li and Clark Verbrugge. 2024. Regular Expressions on Modern GPGPUs. In _16th Workshop on General Purpose Processing Using GPU (GPGPU ’24), March 02, 2024, Edinburgh, United Kingdom._ ACM, New York, NY, USA, 7 pages. https://doi.org/10.1145/3649411.3649416 

## **1 INTRODUCTION** 

Problem domains like network packet inspection have high throughput requirements, filtering packets according to whether they match a given set of regular expressions (REs). In this context GPU-based implementations for RE match determination have been developed and evaluated, showing that despite the sequential nature of RE-matching excellent performance is achievable [5, 1, 2, 4], significantly outcompeting CPU-based designs. Improvements to GPU designs and resource availability, however, mean that optimal implementation is not straightforward, and a naive implementation easily results in low thread occupancy. More recent algorithms can be adapted, but variation in RE structure also challenges the algorithm design, with initial wildcards or other complex structures bottlenecking performance. 

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. _GPGPU ’24, March 02, 2024, Edinburgh, United Kingdom_ 

© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 979-8-4007-1817-5/24/03 https://doi.org/10.1145/3649411.3649416 

## **2 RELATED WORK** 

We have identified prior research efforts in the domain of literal and regex pattern matching. In this section, we will provide a concise overview of their methodologies and potential challenges. 

Regular expressions often include specific substrings, and thus efficient string searching can be a useful part of RE matching. Lin et al. (2013) introduced a parallel approach [10] to the well known Knuth-Morris-Pratt (KMP) algorithm, implementing a CUDA version where each thread extracts a pattern from the pattern array and runs the KMP algorithm on the input string. This method operates effectively when there is a substantial number of patterns to search for. However, if the number of patterns is insufficient, it becomes challenging to fully saturate the computational power of the GPU, particularly in the context of the current exceptionally powerful GPUs. 

In terms of RE matching, Intel has proposed HyperScan[6], a high-performance regular expression matching library. It uses CPU SIMD instructions to achieve high matching performance. However, we will focus more on the GPU algorithms in this study. 

As for GPU algorithms, iNFAnt [5] is an algorithm that is based on compiling regex patterns into NFAs and then using CUDA programs to solve the NFAs. It employs state-level parallelism, meaning that when transitioning between states while processing an input character, tasks are distributed to different threads. This requires the problem size to be sufficiently large to fully utilize the computational power of the GPU. In practice, however, a row in the transition table of a typical regex pattern used in network filtering does not exceed 10 in length, which prevents it from benefiting from larger block sizes, resulting in lower occupancy. 

26 

GPGPU ’24, March 02, 2024, Edinburgh, United Kingdom 

Cheng et al. 

To address iNFAnt’s issue, Liu et al. (2023) introduced ASyncAP [11]. It allocates the text to different blocks, and each thread starts attempting to solve the current NFA from different starting points. If a match cannot be made at a particular step, the thread continues to process the next starting point. As shown in Figure 1, a thread block with a size of nine is searching for the pattern “def” within the input string. T1 starts to match from the first character, T2 starts to match from the second character, and so on. When T1’s match fails, it will start to match from the (1+9) = 10th character. The final result will be that T4 reports a match, and then the kernel returns the result. 

In this way, it is evident that we can benefit from a larger thread block size, thus improving the utilization of computational resources. However, this approach also introduces issues related to additional computational work. Its theoretical time complexity is _𝑂_ ( _𝑚𝑛_[2] ), where _𝑚_ is the size of the NFA, and _𝑛_ is the length of the string. Although, in most cases, it will stop at the first character, if our regex pattern begins with a wildcard element or, worse, starts with a wildcard combined with a quantifier like *, we will have a lot of "easy to reach" states, and the time complexity can easily reach its worst-case, significantly increasing the computational workload and affecting performance. We also note that such regex patterns are not uncommon in various databases. 

**==> picture [253 x 261] intentionally omitted <==**

**Figure 1: Illustration of the ASyncAP** 

## **3 PROPOSED METHOD** 

In this section, we will introduce the limitations of regular expressions and explore the optimization of these limitations through the utilization of prefiltering techniques. We then delve into the specific implementation algorithms for the two types of matching. 

## **3.1 Literal pattern matching** 

While regex patterns provide powerful means of expressing complex and flexible matching conditions, the computational complexity associated with their evaluation is considerably greater than that of literal matching. Regex engines typically involve complex state transitions within finite automata, which, in turn, demand significant processing resources. In contrast, literal matching entails straightforward character-by-character comparison, a task that is computationally less demanding. As an approach to mitigate the computational overhead associated with regex pattern matching, researchers and developers have explored leveraging literal matching as a preliminary "prefilter" stage. In this prefiltering technique, Xu et al. (2023) [17] and Qiu et al. (2021) [12] have demonstrated the remarkable cost-effectiveness of literal matching when compared to its regex counterpart. The results presented in this paper showed that literal string matching, when thoughtfully integrated into pattern-matching pipelines, achieves a performance advantage that is two orders of magnitude superior to regex matching. This cost-effective and efficient strategy has found substantial application in Deep Packet Inspection (DPI) systems, as evidenced by widely utilized applications such as Snort and Suricata. For this stage, there are existing approaches based on SIMD-CPU algorithms based on the FGPA platform[14] [13] [7]. Given the relatively low algorithmic complexity of string matching and GPUs having more computing resources, we implement an optimized version of CUDAKMP [10]. For the prefiltering patterns, we will extract the longest sub-string without special RE symbols from each RE pattern. For example, _configName=_ would be the prefiltering pattern for RE pattern _[?&]configName=[&]+(script|onload|src)[ˆ]_ . If a RE only contains special symbols, we will skip the prefiltering stage. 

In order to solve the limitation of previous CUDA-KMP cannot fully saturate the computational power of the GPU when the number of patterns is insufficient, we propose a string-based parallel approach in which each thread is assigned a segment of the input string for pattern matching. By employing string buffering techniques, we can generate sufficiently long strings to fully utilize the computational capabilities of the GPU. Each sub-string starts from _𝑘_ × _𝑛_ where _𝑘_ ∈ N and _𝑛_ = length of the pattern and has a length of 2× length of the pattern. We then run the KMP algorithm on each thread with the assigned sub-string. This approach ensures that we do not miss the parts connecting two adjacent sub-strings. 

Figure 2 shows an example, searching for the pattern “def” within the input string. Multiple threads will search from different points within the string, and thus a thread may not find the pattern if the pattern instance happens to straddle substring boundaries. This is addressed by adding redundancy to each thread’s search in proportion to the pattern length. A thread is given a sub-string overlapping with the adjacent substring(s) by an amount equal to the length of the pattern. Thus, if we imagine a sliding window of a length equal to the pattern length, starting from the far left and moving to the right, it will always be encompassed by at least one thread’s substring. Since we expect our literal patterns to be much smaller than the input strings the minor redundancy is greatly outweighed by not having to special case the search for partial pattern instances on sub-string boundaries. The detailed algorithm implementation is described by the pseudocode below. 

27 

GPGPU ’24, March 02, 2024, Edinburgh, United Kingdom 

Regular Expressions on Modern GPGPUs 

**Algorithm** CUDAKMP() _target_ ← strings[blockIdx.x] _m_ ← strings_length[blockIdx.x] _stride_ ← blockDim.x **for** _index_ ← _threadIdx.x_ **to** _m_ **by** _stride_ **do** _𝑖_ ← _𝑛_ × index ; _𝑗_ ← _𝑛_ × (index +2) - 1 **if** _𝑖 > 𝑚_ **then return end if** _𝑗 > 𝑚_ **then** _𝑗_ = _𝑚_ **end** _𝑘_ ← 0 **while** _𝑖 < 𝑗_ **do if** _target[i] == pattern[k]_ **then** _𝑖_ + +; _𝑘_ + + **if** _k == n_ **then return** true **end else if** _𝑘 >_ 0 **then** _𝑘_ = _𝑓_ [ _𝑘_ − 1] **else** _𝑖_ + = 1 **end end return** false 

**==> picture [242 x 90] intentionally omitted <==**

**Figure 2: Illustration of the string-based task distribution** 

## **3.2 Regular expression matching** 

Here we describe our approach to addressing the performance concern mentioned in section 2, where performance potentially suffers due to the presence of many easily reachable states in the NFA when a wildcard or a meta-character similar to a wildcard appears at the beginning of the RE. For instance, when there are numerous transitions from the initial state to certain states in the compiled NFA, we will skip the initial, easily reachable states and set the initial state to a more hard-to-get one. We then check whether the previously skipped portion can be satisfied after a successful match. 

Consider the worst case, when the RE starts with a “.*”. In contrast to a case when most threads return after the first or first few characters, in this case every thread will be stuck in the loop of this wildcard trying to match the next element until the entire corpus is checked, and this can increase the workload dramatically. In our 

initial experiments we found that this kind of problem easily erases the performance advantage of ASyncAP, making it worse than the performance of CPU single-thread matching. 

More specifically, we will record the in-degree of each state when compiling the RE into an NFA, and mark it as an easy-to-reach state when the in-degree exceeds a large value (in our case we chose 100). We define a “skip state” (and mark it as such) when an easy-to-reach state is in one of the following two situations: 

1. Connected to the initial state 0 

2. Connected to another skip state 

We extract a reduced NFA from the compiled NFA so that the initial state will not be connected to any easy-to-reach state. A sub-NFA derived from the fragment removed is responsible for the final screening after the reduced NFA finds a match. 

For example, consider the regex pattern: [ˆ abc]+https://t.com. We will first check if it can match https://t.com. If it does, we then continue matching if the character preceding it is one of abc or space and output a match found if it is not. 

In terms of the data structure representation of NFA, ASyncAP [11] chose to use a simple transition table. The potential sparseness of this table may mean it is not memory effective, and in the research results of Blaß and Philippsen [3], they propose sparse representations, such as _COO_ , _ELL_ or others as good ways to represent such graphs. However, in the special case of pattern matching, the situation is different. Assuming a simple ASCII representation, we have a fixed number of nodes, the (at most) 256 characters in the ASCII table. Therefore, we still choose an alphabetical representation similar to the transition table, but only existing edges are stored in the array. This is obviously not applicable when patterns include characters from diverse alphabets, but has the advantage of ensuring efficient access in the many cases when ASCII is sufficient. 

## **4 TUNING COMPILATION CONFIGURATIONS AND RUNNING SETTINGS** 

During the experimental process, we observed that certain compilation and runtime parameter settings significantly impact the algorithm’s performance. Therefore, this section will focus on analyzing the reasons behind these effects and propose optimal configurations. Additionally, the process of identifying optimal configurations from runtime profiling (using NSight Compute) will be elaborated in detail in the following sections. 

## **4.1 Register Counts per Thread** 

Firstly, we identified a crucial aspect, namely, the number of registers per thread. As the number of registers per thread increases, it allows for more reading and writing of necessary data within registers, thereby reducing memory access. However, the number of registers per thread also limits the number of threads that can simultaneously run within each streaming multiprocessor (SM), as each multiprocessor has a finite number of 32-bit registers, totaling 65,536. 

For instance, on our experimental machine (see table 1), the default number of registers per thread is 74. If we set the number of threads per block to 1024, since 1024 * 74 > 65,536, we would not have enough registers to execute the kernel, leading to program errors and termination. 

28 

GPGPU ’24, March 02, 2024, Edinburgh, United Kingdom 

Cheng et al. 

A trade-off is necessary to choose an optimal number of registers per thread. Profiling shows the relationship between register count and occupancy. As illustrated in the “Impact of Varying Registers Per Thread” section of Figure 3, we set the number of threads per block to be 512. As the number of registers per thread increased from 1 to 40, although the theoretical occupancy remained 100%, a higher number of registers per thread resulted in a higher cache hit rate, leading to better performance. The optimal solution was achieved when the number of registers per thread reached 42. At this point, we could have 3 thread blocks per multiprocessor (i.e., 65536/512/42 = 3), and the cache hit rate was higher compared to lower numbers of registers per thread, indicating reduced memory read/write operations. However, as this number continued to rise from 42 to 64, we were constrained to 2 thread blocks per multiprocessor. Despite the increasing cache hit rate, the reduction in the number of thread blocks led to decreased task parallelism, resulting in lower occupancy, and increasing from 64 to 128 only continues this trend. Therefore, the optimal strategy is to maximize occupancy while having as many registers per thread as possible. We can easily identify the maximum possible number of registers while maximizing occupancy using NSight Compute. 

## **4.2 Block Size** 

The block size also significantly impacts occupancy, thus affecting performance. When the block size is too small, we may not be able to run a sufficient number of blocks on the SM due to shared memory size limitations, resulting in underutilization of threads. On the other hand, when the block size becomes sufficiently large to achieve a theoretical occupancy of 100%, further increasing the block size may lead to alignment issues between blocks, causing some threads to idle. However, as the block size continues to increase, the theoretical occupancy may once again return to 100 when the value is appropriate. 

To illustrate, envision filling a large, 2m x 2m area with smaller squares. Using squares of size 0.5m we can fill it exactly, while increasing our squares to have a side length of 0.6m will mean we cannot completely fill the large square. If we continue to increase the side length to 1m, we once again perfectly fill the large square. 

Because our experimental machine uses a GPU with CUDA compute capability 8.6, according to the official CUDA documentation, each SM can have 48 warps running simultaneously, each of 32 threads, giving 48*32=1536 threads. Thus we need to divide 1536 by the block size to perfectly fill the entire SM without leaving gaps. Each thread block can use up to 99 KB of shared memory, and our algorithm requires 32 KB for each thread, so we can have at most 3 thread blocks, so we choose 1536/3=512 as our block size. The optimal setting for this data can be found in Figure 3 in the “Impact of Varying Block Size” section. 

## **4.3 Shared Memory Usage per Block** 

As mentioned in the Block Size section above, each SM has a limited amount of shared memory. Consequently, the size of shared memory used by each block also affects the maximum number of blocks that can run simultaneously. Therefore, when designing algorithms, it is crucial to carefully balance the relationship between block size and the amount of shared memory used per block. Again, profiling 

results in Figure 3 shows the optimal configuration, this time under “Impact of Varying Shared Memory Usage per Block” section. 

## **5 PERFORMANCE EVALUATION** 

In this section, we describe our experiments evaluating our design changes experiments, including comparisons with the existing designs, and with CPU-based parallelism as well as an additional baseline. We have tested the GPU version of the methods and all get the same correct results as the CPU version and verified that literal strings exploited in the prefiltering stage appear in all hits as expected. Every approach uses the optimal configuration parameters mentioned in the previous section. 

CPU Intel Core i5-10500H Memory DDR4 8GB x 2 GPU NVidia GeForce RTX 3060 Laptop **Table 1: Hardware specifications** OS Ubuntu 22.04.3 LTS Driver NVIDIA Display Driver version 535.104.05 SDK CUDA 12.2 Tool NSight Compute 2023.2.2 **Table 2: Software specifications** 

Tables 1 and 2 list the hardware and software specifications. In terms of the dataset, the test suite chosen by iNFAnt is no longer available. The corpus [15] used by ASyncAP are binary files that are incompatible with the tests conducted in this study. To facilitate comparison with other approaches to RE evaluation on GPUs that focus on deep packet inspection, we based our evaluation on 3,379 regex patterns obtained from Snort [16], which is the same as ASyncAP, and generated a representative corpus primarily consisting of HTTP code, SQL queries, etc., as input using the ChatGPT API [8]. Performance testing for each algorithm was conducted using NSightCompute 2023.2.2. 

## **5.1 Literal pattern matching** 

As stated in section 3.1, we extract the longest string without special symbols from the regex pattern as the prefilter pattern during the regex compilation process, which does not correlate with the length of the regex pattern. Moreover, the time complexity of KMP only depends on the length of the string, not the length of the pattern. Therefore, we do not conduct experiments with the length and type of regex as variables. The main difference between the patternbased and string-based methods is that the string-based method can use a buffer to ensure a large enough block size, while the patternbased method cannot guarantee it when the number of patterns is small. Therefore, we only compare the impact of different block sizes on occupancy under the same text. 

29 

GPGPU ’24, March 02, 2024, Edinburgh, United Kingdom 

Regular Expressions on Modern GPGPUs 

**==> picture [404 x 169] intentionally omitted <==**

**Figure 3: NSight Compute Occupancy Analysis** 

**==> picture [194 x 114] intentionally omitted <==**

**Figure 4: CUDA-KMP performance over #threads/block** 

**==> picture [194 x 113] intentionally omitted <==**

**Figure 5: CUDA-KMP occupancy over #threads/block** 

The experimental results shown in figures 4 and 5 show that when the number of regex patterns is less than or equal to 64, the block size of the pattern-based method is too small, and only a limited number of blocks can be launched on the same SM, resulting in a low level of occupancy. Only when the number of regex patterns is greater than or equal to 128, can the pattern-based method achieve the maximum occupancy. Therefore, our method has a significant advantage of about 2x-40x speedup compared to the pattern-based method when the number of regex patterns is less than 128 (depending on the different number of regex patterns). 

|CPU|1823ms|
|---|---|
|CUDA-KMP|22ms|



**Table 3: CPU vs CUDA** 

We also established a CPU version experiment to highlight the advantages of CUDA computation. Due to the inability to independently evaluate the CPU version of the KMP algorithm using NSightCompute, for this experiment we relied on the runtime measurements obtained from the code for both the CPU and CUDA versions. For the CUDA version, this includes the additional overhead of invoking GPU methods. As indicated in table 3, relative to the CPU version, CUDA-KMP still exhibits approximately an 82x performance improvement. 

## **5.2 Regular expression matching** 

As for the regular expression matching part, we also employed a CPU single-thread version as a control group to compare the performance of iNFAnt, ASyncAP, and ASyncAP-Optimized, of which ASyncAP-Optimized is the method we proposed. For this experiment, we categorized the regex patterns into three groups: small (fewer than 100 edges), medium (100 to 500 edges), and large (more than 500 edges), where edges refer to transitions among different states. The experimental results are shown in the table 4. Additionally, we divided them into two categories based on whether the initial state is 0 (meaning it starts with a wildcard) or not. These results are shown for the larger RE patterns under columns L and LW. The time consumption in the tables refers to the average time it takes for each regex pattern to match the corpus among 100 regex patterns. Note that we did not use NSight Compute to measure the performance for the LW column of table 4, because NSightCompute requires multiple iterations to average test performance, and ASyncAP performed so poorly in this set of tests that NSightCompute would freeze. 

30 

GPGPU ’24, March 02, 2024, Edinburgh, United Kingdom 

Cheng et al. 

||S|M|L|LW|
|---|---|---|---|---|
|CPU|5028ms|5523ms|7532ms|7334ms|
|iNFAnt|768ms|810ms|1301ms|1218ms|
|ASyncAP|18ms|25ms|38ms|71946ms|
|ASyncAP_Optimized|20ms|26ms|40ms|38ms|



**Table 4: Performance with different RE size (LW stands for Large with Wildcard)** 

|RE_ID|ASyncAP|ASyncAP_Optimized|
|---|---|---|
|184|59886ms|24ms|
|1637|129885ms|36ms|
|2421|33456ms|65ms|
|19|123289ms|36ms|
|2416|33453ms|65ms|
|1584|153479ms|59ms|
|266|128636ms|26ms|
|1815|525ms|27ms|
|197|536ms|27ms|
|1802|56307ms|15ms|



**Table 5: Detailed ASyncAP vs ASyncAP_Optimized** 

block when a hit is detected by some other thread. But if the buffered string is not long enough, the computation workload reduced by the early return is not enough to compensate for the overhead caused by the condition check and the early return, which leads to a worse performance. On the other hand, when the buffered string is long enough, the algorithm’s performance improves with the increase of the hit rate. 

We also added a group of experimental groups with different RE sizes to show the performance of using pre-filtering technology6. We found that because prefiltering removed most of the RE matching workload, the impact of the RE matching part became less noticeable so the time consumption of different algorithms and different RE sizes was less divergent. Therefore, it has a better acceleration effect on algorithms with poorer performance, such as the iNFAnt algorithm, which has an acceleration of about 10x faster. For ASyncAP and ASyncAP Optimized, although the acceleration is smaller (about 80%), the performance is still 8x faster than iNFAnt.[˜] 

||S|M|L|
|---|---|---|---|
|iNFAnt|84.6ms|113.5ms|149.8ms|
|ASyncAP|10.1ms|14.2ms|16.8ms|
|ASyncAP_Optimized|10.2ms|14.2ms|17ms|



**Table 6: RE matching with prefiltering** 

We observe that in most cases the use of ASyncAP results in dramatically better performance than either CPU or iNFAnt. The benefits of our ASyncAP-Optimized version become apparent, however, when regex patterns start with a wildcard. More specifically, we note that for each different regex pattern in (table 5), ASyncAPOptimized can achieve a 19x to 20x acceleration if it only starts with one or more wildcards. But if it starts with wildcards combined with a quantifier, ASyncAP-Optimized can achieve about 3600x speedup, resulting in a 1900x acceleration shown in (table 4). The REs with ID are available in the GitHub repository[9]. 

To validate the perspective that the iNFAnt algorithm cannot benefit from larger block sizes and, therefore, results in lower occupancy, we also conducted experiments with different block sizes under the same input regex patterns and datasets. The results are displayed in the following figure: 

**==> picture [194 x 113] intentionally omitted <==**

**Figure 6: iNFAnt execution time over #threads/block** 

## **6 CONCLUSION** 

In this paper, we compared various existing methods for literal and regex pattern matching. Through our optimization, their performance was significantly improved, particularly in terms of their robustness and adaptability to a wider range of search scenarios. Our evaluation confirms the much greater performance achieved by utilizing CUDA programming in comparison to CPU for solving pattern-matching problems, although in this process, we also discovered that certain compilation and runtime parameter settings significantly impact the algorithm’s performance. The latter necessitates a more prudent configuration of parameters to optimize performance. 

## **7 FUTURE WORK** 

It might be valuable to explore the application of our research on newer hardware platforms to examine the stability and generalizability of our findings. Investigating the implementation of auto-tuning mechanisms for parameter optimization could offer insights into enhancing adaptability. The success of pre-filtering also suggests there exists an opportunity to extend our analysis beyond literal strings to identify and exploit other inexpensive sub-patterns in regular expressions, potentially improving overall matching efficiency. Diversifying our experiments to include regular expressions from various domains, such as those originating from web engine DOM-searches, could contribute to a more comprehensive understanding of the methodology’s versatility. 

## **ACKNOWLEDGMENTS** 

For both of the matching stages, we also noticed that the length of the buffered string affects the performance. For each buffered string, we perform an early return for all the threads in the current 

This work is supported by the Natural Sciences and Engineering Research Council of Canada (NSERC). 

31 

GPGPU ’24, March 02, 2024, Edinburgh, United Kingdom 

Regular Expressions on Modern GPGPUs 

## **REFERENCES** 

- [1] Matteo Avalle, Fulvio Risso, and Riccardo Sisto. 2015. Scalable Algorithms for NFA Multi-Striding and NFA-Based Deep Packet Inspection on GPUs. _IEEE/ACM Transactions on Networking_ 24 (06 2015), 1–1. https://doi.org/10.1109/TNET.2015. 2429918 

- [2] Michela Becchi, Mark Franklin, and Patrick Crowley. 2008. A workload for evaluating deep packet inspection architectures. In _2008 IEEE International Symposium on Workload Characterization_ . 79–89. https://doi.org/10.1109/IISWC.2008.4636093 

- [3] Thorsten Blaß and Michael Philippsen. 2019. Which Graph Representation to Select for Static Graph-Algorithms on a CUDA-Capable GPU. In _Proceedings of the 12th Workshop on General Purpose Processing Using GPUs_ (Providence, RI, USA) _(GPGPU ’19)_ . Association for Computing Machinery, New York, NY, USA, 22–31. https://doi.org/10.1145/3300053.3319416 

- [4] Anat Bremler-Barr, Yotam Harchol, David Hay, and Yaron Koral. 2014. Deep Packet Inspection as a Service. In _Proceedings of the 10th ACM International on Conference on Emerging Networking Experiments and Technologies_ (Sydney, Australia) _(CoNEXT ’14)_ . Association for Computing Machinery, New York, NY, USA, 271–282. https://doi.org/10.1145/2674005.2674984 

- [5] Niccolò Cascarano, Pierluigi Rolando, Fulvio Risso, and Riccardo Sisto. 2010. INFAnt: NFA Pattern Matching on GPGPU Devices. _SIGCOMM Comput. Commun. Rev._ 40, 5 (oct 2010), 20–26. https://doi.org/10.1145/1880153.1880157 

   - [13] R. Sidhu and V.K. Prasanna. 2001. Fast Regular Expression Matching Using FPGAs. In _The 9th Annual IEEE Symposium on Field-Programmable Custom Computing Machines (FCCM’01)_ . 227–238. 

   - [14] David Sidler, Zsolt István, Muhsen Owaida, and Gustavo Alonso. 2017. Accelerating Pattern Matching Queries in Hybrid CPU-FPGA Architectures. In _Proceedings of the 2017 ACM International Conference on Management of Data_ (Chicago, Illinois, USA) _(SIGMOD ’17)_ . Association for Computing Machinery, New York, NY, USA, 403–415. https://doi.org/10. 1145/3035918.3035954 

   - [15] Jack Wadden. 2017. https://github.com/jackwadden/ ANMLZoo/tree/master/Snort/inputs. 

   - [16] Jack Wadden. 2017. Snort Regex Patterns. https: //github.com/jackwadden/ANMLZoo/blob/master/Snort/ regex/snort.1chip.regex. 

   - [17] Hao Xu, Harry Chang, Wenjun Zhu, Yang Hong, Geoff Langdale, Kun Qiu, and Jin Zhao. 2023. Harry: A Scalable SIMDbased Multi-literal Pattern Matching Engine for Deep Packet Inspection. In _IEEE INFOCOM 2023 - IEEE Conference on Computer Communications, New York City, NY, USA, May 17-20, 2023_ . IEEE, 1–10. https://doi.org/10.1109/INFOCOM53939. 2023.10229022 

- [6] Intel. 2017. HyperScan. https://github.com/intel/hyperscan. 

- [7] Aajna Karki, Chethan Palangotu Keshava, Spoorthi Mysore Shivakumar, Joshua Skow, Goutam Madhukeshwar Hegde, and Hyeran Jeon. 2019. Detailed Characterization of Deep Neural Networks on GPUs and FPGAs. In _Proceedings of the 12th Workshop on General Purpose Processing Using GPUs_ (Providence, RI, USA) _(GPGPU ’19)_ . Association for Computing Machinery, New York, NY, USA, 12–21. https://doi.org/10.1145/3300053. 3319418 

- [8] Cheng Li. 2023. https://github.com/cli117/thesis_work/blob/ main/iNFAnt_Buffer/test_suite/midstr_7k.txt. 

- [9] Cheng Li. 2023. https://github.com/cli117/thesis_work/tree/ main/iNFAnt_Buffer/test_suite/nfa_output. 

- [10] Kuan-Ju Lin, Yi-Hsuan Huang, and Chun-Yuan Lin. 2013. Efficient Parallel Knuth-Morris-Pratt Algorithm for Multi-GPUs with CUDA. In _Advances in Intelligent Systems and Applications - Volume 2_ , Jeng-Shyang Pan, Ching-Nung Yang, and Chia-Chen Lin (Eds.). Springer Berlin Heidelberg, Berlin, Heidelberg, 543–552. 

- [11] Hongyuan Liu, Sreepathi Pai, and Adwait Jog. 2023. Asynchronous Automata Processing on GPUs. _Proc. ACM Meas. Anal. Comput. Syst._ 7, 1, Article 27 (mar 2023), 27 pages. https://doi.org/10.1145/3579453 

- [12] Kun Qiu, Harry Chang, Yang Hong, Wenjun Zhu, Xiang Wang, and Baoqian Li. 2021. Teddy: An Efficient SIMD-Based Literal Matching Engine for Scalable Deep Packet Inspection. In _Proceedings of the 50th International Conference on Parallel Processing_ (Lemont, IL, USA) _(ICPP ’21)_ . Association for Computing Machinery, New York, NY, USA, Article 62, 11 pages. https://doi.org/10.1145/3472456.3473512 

32 

