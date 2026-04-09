# 抽出されたLaTeXテーブル

以下のテーブル構造をLLMやPandas等でMarkdown化する際の入力基板として利用できます。

## Table 1
```latex
\begin{table}[t]
\centering
\small
\resizebox{\columnwidth}{!}{%
\begin{tabular}{ll|cc}
\toprule
& & \multicolumn{2}{c}{\textbf{Avg. Tokens / Task}} \\
\cmidrule(lr){3-4}
\textbf{Method} & \textbf{Task Setting} & \textbf{Opus 4.6} & \textbf{Sonnet 4.6} \\
\midrule
\multirow{2}{*}{ReAct}
 & Batch 1 & 8298 & 6893 \\
 & Batch 2 & 7022 & 7029 \\
\midrule
\multirow{2}{*}{Self-Evolving Agents}
 & Batch 1 (from scratch) & 8608 & 8163 \\
 & Batch 2 (w/ saved) & 6210 & 8223 \\
\midrule
\multirow{2}{*}{AgentFactory}
 & Batch 1 (from scratch) & 4324 & 9199 \\
 & Batch 2 (w/ saved) & 2971 & 3862 \\
\bottomrule
\end{tabular}%
}
\caption{Average output tokens per task across evaluation configurations. Lower values indicate that the orchestrating agent requires less effort to complete tasks, reflecting more efficient subagent reuse. Token counts exclude subagent-internal LLM consumption.}
\label{tab:eval}
\end{table}
```

## Table 2
```latex
\begin{table*}[t]
\centering
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{0.85}
\footnotesize
\begin{tabular}{c|p{14.2cm}}
\toprule
\textbf{\#} & \textbf{Task Description} \\
\midrule
1 & Among various online discussions about the housing price bubble, how has public sentiment changed over time? Generate an analysis report and a trend chart, and include discussion and summary in the report. \\
2 & Search for and open the Stanford CS231n course homepage, find the syllabus or lecture list, and output the topics and corresponding links for the first 5 lectures. Save the final results to a markdown file. \\
3 & Book a Tencent Meeting for tomorrow at 4 PM with the topic ``Work Meeting''. Find the meeting booking entry on the Tencent Meeting web version, then complete the booking through browser automation. Output the meeting invitation details, meeting ID, and meeting link. \\
4 & Search for China's historical population data, then use matplotlib to plot the population change curve. \\
5 & Search for Bitcoin's price data over the past 5 years, use matplotlib to plot the price trend, and calculate the annualized volatility. \\
6 & Search for and download trending keyword frequency data from a social media platform, and display the top 20 using a bar chart. \\
7 & Search for and download China's education expenditure and GDP data, plot a scatter chart showing the relationship between the two, and fit a regression line. \\
8 & Write a Python mini-game: Tetris, with keyboard controls and basic scoring logic. \\
9 & Search for and open Wikipedia, find the ``Transformer (machine learning model)'' page, extract its core definition, and summarize the main ideas of Self-Attention. Save the results to a markdown file. \\
10 & Search for and open the GitHub website, find OpenAI's official organization page, and output the page's description and a list of main repositories (at least 5). Save the results to a markdown file. \\
11 & Search for and open the HuggingFace website, find a ``Text-to-Image'' model leaderboard or collection page, and summarize the 3 most common model architectures. Save the results to a markdown file. \\
12 & Create a soothing bedtime meditation audio file (15--20 min), featuring gentle guided breathing exercises, progressive muscle relaxation instructions, and calming visualizations. \\
13 & Complete a task whose detailed description is provided in <audio\_file\_path>. \\
14 & Search travel resources about Tokyo. Under a budget of \$100 USD, plan a 3-day itinerary with at least one cultural attraction per day, total travel time under 5 hours, and at least one anime-related location. Output the itinerary, budget breakdown, and total travel time. \\
15 & Search and download CO\textsubscript{2} emissions and renewable energy share data for at least 5 countries. Analyze the correlation, generate a plot, and summarize the findings. \\
\bottomrule
\end{tabular}
\caption{Batch~1 evaluation tasks (15 tasks) used for initial subagent construction.}
\label{tab:tasks-batch1}
\end{table*}
```

## Table 3
```latex
\begin{table*}[t]
\centering
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{0.85}
\footnotesize
\begin{tabular}{c|p{14.2cm}}
\toprule
\textbf{\#} & \textbf{Task Description} \\
\midrule
1 & Among various online discussions about electric vehicle adoption, how has public sentiment changed over time? Generate an analysis report and a trend chart, and include discussion and summary in the report. \\
2 & Search for and open the MIT 6.S191 (Introduction to Deep Learning) course homepage, find the syllabus or lecture list, and output the topics and corresponding links for the first 5 lectures. Save the final results to a markdown file. \\
3 & Book a Tencent Meeting for tomorrow at 7 PM with the topic ``Work Meeting''. Find the meeting booking entry on the Tencent Meeting web version, then complete the booking through browser automation. Output the meeting invitation details, meeting ID, and meeting link. \\
4 & Search for Japan's historical population data, then use matplotlib to plot the population change curve. \\
5 & Search for Ethereum's price data over the past 5 years, use matplotlib to plot the price trend, and calculate the annualized volatility. \\
6 & Search for and download trending topic data from a Chinese social media platform, and display the top 20 using a bar chart. \\
7 & Search for and download the US healthcare expenditure and GDP data, plot a scatter chart showing the relationship between the two, and fit a regression line. \\
8 & Write a Python mini-game: Snake, with keyboard controls and basic scoring logic. \\
9 & Search for and open Wikipedia, find the ``BERT (language model)'' page, extract its core definition, and summarize the main ideas of the Transformer architecture. Save the results to a markdown file. \\
10 & Search for and open the GitHub website, find Meta AI's official organization page, and output the page's description and a list of main repositories (at least 5). Save the results to a markdown file. \\
11 & Search for and open the HuggingFace website, find a ``Text-to-Speech'' model leaderboard or collection page, and summarize the 3 most common model architectures. Save the results to a markdown file. \\
12 & Create a focus-enhancing background audio file (15--20 min), featuring gentle ambient sounds, subtle background music, and nature sounds to help concentrate. \\
13 & Complete a task whose detailed description is provided in <audio\_file\_path>. \\
14 & Search travel resources about Paris. Under a budget of \$150 USD, plan a 3-day itinerary with at least one museum per day, total travel time under 6 hours, and at least one historic landmark. Output the itinerary, budget breakdown, and total travel time. \\
15 & Search and download GDP per capita and life expectancy data for at least 5 countries. Analyze the correlation between economic development and health outcomes, generate a plot, and summarize the findings. \\
\bottomrule
\end{tabular}
\caption{Batch~2 evaluation tasks (15 tasks) used as transfer evaluation targets. Each task mirrors the structure of its Batch~1 counterpart but differs in specific requirements.}
\label{tab:tasks-batch2}
\end{table*}
```

