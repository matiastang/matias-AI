<!--
 * @Author: matiastang
 * @Date: 2022-08-05 15:34:59
 * @LastEditors: matiastang
 * @LastEditTime: 2022-08-05 15:41:18
 * @FilePath: /matias-AI/md/GPT.md
 * @Description: GPT
-->
# GPT

在介绍BERT之前，我们先看看另外一套方案。我在第一部分说过，BERT并不是第一个提出预训练加微调的方案，此前还有一套方案叫GPT，这也是BERT重点对比的方案，文章在这，Improving Language Understanding by Generative Pre-Training（https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf）。GPT的模型结构和BERT是相同的，都是图2.10的结构，只是BERT的模型规模更加庞大。GPT是这么预训练的，在一个8亿单词的语料库上做训练，给出前文，不断地预测下一个单词。比如这句话，Winter is coming，当给出第一个词Winter之后，预测下一个词is，之后再预测下一个词coming。不需要标注数据，通过这种无监督训练的方式，得到一个预训练模型。

我们再来看看BERT有什么不同。BERT来自于Bidirectional Encoder Representations from Transformers首字母缩写，这里提到了一个双向（Bidirectional）的概念。BERT在一个33亿单词的语料库上做预训练，语料库就要比GPT大了几倍。预训练包括了两个任务，第一个任务是随机地扣掉15%的单词，用一个掩码MASK代替，让模型去猜测这个单词；第二个任务是，每个训练样本是一个上下句，有50%的样本，下句和上句是真实的，另外50%的样本，下句和上句是无关的，模型需要判断两句的关系。这两个任务各有一个loss，将这两个loss加起来作为总的loss进行优化。下面两行是一个小栗子，用括号标注的是扣掉的词，用[MASK]来代替。