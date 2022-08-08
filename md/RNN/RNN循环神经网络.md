<!--
 * @Author: matiastang
 * @Date: 2021-12-15 11:39:23
 * @LastEditors: matiastang
 * @LastEditTime: 2022-08-08 17:07:31
 * @FilePath: /matias-AI/md/RNN/RNN循环神经网络.md
 * @Description: 循环神经网络
-->
# 循环神经网络

[LSTM和GRU的解析从未如此通俗易懂（动图）](http://www.360doc.com/content/19/0330/20/7669533_825345291.shtml)

`循环神经网络`实际上`前馈全连接神经网络`的一种扩展，如果你已经掌握了全连接神经网络中的算法、公式推导等知识，那么学习循环神经网络会很容易。这也是为什么本书花了很多篇幅在全连接神经网络上打基础的原因。如果说**全连接网络是学习静态数据的非线性特征**的，那么**循环神经网络就是学习动态序列数据的非线性特征**的。

`不定长时序循环神经网络`、`深度循环神经网络`、`双向循环神经网络`。
高级循环神经网络部分，将介绍`LSTM`、`GRU`、`序列到序列`的模型的原理，为以后学习**自然语言处理（Natural Language Processing，NLP）**打下坚实的基础。

## 前馈神经网络的不足

`神经网络的输入都是一个或者一批静态的数据`

## 循环神经网络的发展简史
循环神经网络（RNN，Recurrent Neural Network）的历史可以简单概括如下：

1933年，西班牙神经生物学家Rafael Lorente de Nó发现大脑皮层（cerebral cortex）的解剖结构允许刺激在神经回路中循环传递，并由此提出反响回路假设（reverberating circuit hypothesis）。
1982年，美国学者John Hopfield使用二元节点建立了具有结合存储（content-addressable memory）能力的神经网络，即Hopfield神经网络。
1986年，Michael I. Jordan基于Hopfield网络的结合存储概念，在分布式并行处理（parallel distributed processing）理论下建立了新的循环神经网络，即Jordan网络。
1990年，Jeffrey Elman提出了第一个全连接的循环神经网络，Elman网络。Jordan网络和Elman网络是最早出现的面向序列数据的循环神经网络，由于二者都从单层前馈神经网络出发构建递归连接，因此也被称为简单循环网络（Simple Recurrent Network, SRN）。
1990年，Paul Werbos提出了循环神经网络的随时间反向传播（BP Through Time，BPTT），BPTT被沿用至今，是循环神经网络进行学习的主要方法。
1991年，Sepp Hochreiter发现了循环神经网络的长期依赖问题（long-term dependencies problem），大量优化理论得到引入并衍生出许多改进算法，包括`神经历史压缩器（Neural History Compressor, NHC）`、`长短期记忆网络（Long Short-Term Memory networks, LSTM）`、`门控循环单元网络（Gated Recurrent Unit networks, GRU）`、`回声状态网络（echo state network）`、`独立循环神经网络（Independent RNN）`等。

## RNN 和 Transformer 对比

到这里就把Transformer的结构讲完了，同样都是做NLP任务，我们来和RNN做个对比。图2.8是个最基本的RNN结构，还有计算公式。当计算隐向量h4时，用到了输入x4，和上一步算出来的隐向量h3，h3包含了前面所有节点的信息。h4中包含最多的信息是当前的输入x4，越往前的输入，随着距离的增加，信息衰减得越多。对于每一个输出隐向量h都是如此，包含信息最多得是当前的输入，随着距离拉远，包含前面输入的信息越来越少。但是Transformer这个结构就不存在这个问题，不管当前词和其他词的空间距离有多远，包含其他词的信息不取决于距离，而是取决于两者的相关性，这是Transformer的第一个优势。第二个优势在于，对于Transformer来说，在对当前词进行计算的时候，不仅可以用到前面的词，也可以用到后面的词。而RNN只能用到前面的词，这并不是个严重的问题，因为这可以通过双向RNN来解决。第三点，RNN是一个顺序的结构，必须要一步一步地计算，只有计算出h1，才能计算h2，再计算h3，隐向量无法同时并行计算，导致RNN的计算效率不高，这是RNN的固有结构所造成的，之前有一些工作就是在研究如何对RNN的计算并行化。通过前文的介绍，可以看到Transformer不存在这个问题。通过这里的比较，可以看到Transformer相对于RNN有巨大的优势，因此我看到有人说RNN以后会被取代。

关于上面的第三点优势，可能有人会不认可，RNN的结构包含了序列的时序信息，而Transformer却完全把时序信息给丢掉了。为了解决时序的问题，Transformer的作者用了一个绝妙的办法，这就是我在前文提到的位置编码（Positional Encoding）。位置编码是和word embedding同样维度的向量，将位置embedding和词embedding加在一起，作为输入embedding，如图2.9所示。位置编码可以通过学习得到，也可以通过设置一个跟位置或者时序相关的函数得到，比如设置一个正弦或者余弦函数，这里不再多说。

## 循环神经网络的结构和典型用途

### 一对多的结构

### 多对一的结构

### 多对多（输入输出等量）

### 多对多（输入输出不等量）

这是循环神经网络最重要的一个变种，又叫做`编码解码（Encoder-Decoder）模型`，或者`序列到序列（seqence to seqence）模型`。

## 高级循环神经网络概述

循环神经网络的由来和发展历史，传统循环神经网络的原理和应用。**循环神经网络弥补了前馈神经网络的不足，可以更好的处理`时序相关的问题`，扩大了神经网络解决问题的范围。**

**传统的循环神经网络也有自身的缺陷，由于容易产生`梯度爆炸`和`梯度消失`的问题，导致很难处理长距离的依赖。**

**科学家们对普通循环神经网络进行改进，以便处理更复杂场景的数据的模型，提出了如`LSTM`, `GRU`, `Seq2Seq`等模型。此外，`注意力（Attention）机制`的引入，使得Seq2Seq模型的性能得到提升**

`自注意力`、`多头注意力`