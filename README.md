# Towards Making the Most of ChatGPT for Machine Translation

<b>Towards Making the Most of ChatGPT for Machine Translation</b>. ([Full report](https://github.com/Romainpkq/ChatGPT4MT/sources/report.pdf))

This repository releases the testsets evaluated by [ChatGPT](https://chat.openai.com/chat) API (gpt-3.5-turbo-0301),  for the replication of the study.

## Abstract

ChatGPT shows remarkable capabilities for machine translation (MT). Several prior studies have shown that it achieves comparable results to commercial systems for high-resource languages, but lags behind in complex tasks, e.g, low-resource and distant-language-pairs translation. However, **they usually adopt simple prompts which can not fully elicit the capability of ChatGPT**. In this report, we aim to further mine ChatGPT's translation ability by revisiting several aspects: temperature, task information, and domain information, and correspondingly propose two *<font color=red>(simple but effective)</font>* prompts: *Task-Specific Prompts* (TSP) and *Domain-Specific Prompts* (DSP). We show that: 1. The performance of ChatGPT depends largely on temperature, and a lower temperature usually can achieve better performance; 2. Emphasizing the task information further improves ChatGPT's performance, particularly in complex MT tasks; 3. Introducing domain information can elicit ChatGPT's generalization ability and improve its performance in the specific domain; 4. ChatGPT tends to generate hallucinations for non-English-centric MT tasks, which can be partially addressed by our proposed prompts but still need to be highlighted for the MT/NLP community.
We also explore the effects of advanced in-context learning strategies and find a <font color=red>(negative but interesting)</font> observation: the powerful chain-of-thought prompt leads to word-by-word translation behavior, thus bringing significant translation degradation.

## Data and Evaluations

We evaluate the performance of the models on the [Flores-200](https://github.com/facebookresearch/flores/tree/main/flores200) and [WMT19 Bio](https://www.statmt.org/wmt19/biomedical-translation-task.html) and  [News](https://www.statmt.org/wmt19/translation-task.html) test sets. The task statistics are shown as follows:


<div align="center">
    <img width="80%" alt="image" src="./figures/datasets.png">
</div>

