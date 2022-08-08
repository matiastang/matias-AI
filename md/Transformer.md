<!--
 * @Author: matiastang
 * @Date: 2022-08-04 16:32:28
 * @LastEditors: matiastang
 * @LastEditTime: 2022-08-05 10:34:26
 * @FilePath: /matias-AI/md/Transformer.md
 * @Description: Transformer
-->
# Transformer

[transformer](https://arxiv.org/pdf/1706.03762.pdf)
[重要论文-Transformer](https://jalammar.github.io/illustrated-transformer/)

![矩阵形式的self-attention计算](../md/images/矩阵形式的self-attention计算.png)
其中`T`是变量，及`Kt`为单词的对应的`K`矩阵

## Encoder-Decoder

1.1 简介
Encoder-Decoder框架顾名思义就是编码-解码框架，目前大部分attention模型都是依附于Encoder-Decoder框架进行实现，在NLP中Encoder-Decoder框架主要被用来处理序列-序列问题。也就是输入一个序列，生成一个序列的问题。这两个序列可以分别是任意长度。

具体到NLP中的任务比如：文本摘要 文本翻译 问答系统
Encoder-Decoder框架不仅仅在文本领域广泛使用，在语音识别、图像处理等领域也经常使用。比如对于语音识别来说，区别无非是Encoder部分的输入是语音流，输出是对应的文本信息；而对于“图像描述”任务来说，Encoder部分的输入是一副图片，Decoder的输出是能够描述图片语义内容的一句描述语。一般而言，文本处理和语音识别的Encoder部分通常采用RNN模型，图像处理的Encoder一般采用CNN模型。

### Encoder：

编码器，对于输入的序列<x1, x2, x3 … xn>进行编码，使其转化为一个语义编码C，C中储存了序列<x1, x2, x3 … xn>的信息

Encoder编码方式有很多种，在文本处理领域主要有RNN / LSTM / GRU / BiRNN / BiLSTM / BiGRU

以 RNN 为例，输入<x1, x2, x3, x4>，通过RNN生成隐藏层的状态值<h1, h2, h3, h4>，如何确定语义编码C呢？最简单的办法是直接用最后时刻输出的 ht 作为 C 的状态值，这里也就是可以用 h4 直接作为语义编码C的值，也可以将所有时刻隐藏层的值进行汇总，然后生成语义编码C的值，这里就是C = q (h1, h2, h3, h4 )，q是非线性激活函数。

得到了语义编码C之后，要在Decoder中对语义编码C进行解码

### Decoder：

解码器，根据输入的语义编码C，然后将其解码成序列数据，解码方式也可以采用RNN / LSTM / GRU / BiRNN / BiLSTM / BiGRU。Decoder和Encoder的编码解码方式可以任意组合。

基于 `seq2seq(Sequence to Sequence)` 模型有两种解码方式：
1. 方法1论文-Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation
论文1中指出，因为语义编码C包含了整个输入序列的信息，所以在解码的每一步都引入C。文中 Ecoder-Decoder 均是使用RNN，在计算每一时刻的输出 yt 时，都应该输入语义编码C，即 ht = f(ht-1, yt-1, C)，p(yt) = f(ht, yt−1, C)。ht为当前 t 时刻的隐藏层的值，yt-1为上一时刻的预测输出，作为t时刻的输入，每一时刻的语义编码C是相同的。这类似于人类看到眼前的画面，但是眼中却没有注意焦点一样。
2. 方法2论文-Sequence to Sequence Learning with Neural Networks
论文2的方式相对简单，只在Decoder的初始输入引入语义编码C，将语义编码C作为隐藏层状态值 h0 的初始值，p(yt) = f(ht,yt−1)

### 缺点


1. 按照方法1解码，每一时刻的输出如上式所示，可以看出，在生成目标句子单词时，使用的语义编码C都是一样的，没有任何区别。而语义编码C是由输入序列X的每个单词经过Encoder 编码产生的，输入序列X中任意单词对生成某个目标单词 yi 来说影响力都是相同的，没有任何区别
`（如果Encoder是RNN的话，理论上后输入的单词影响越大，并非等权的，估计这也是为何Google提出 Sequence to Sequence 模型时发现把输入句子逆序输入做翻译效果会更好的小Trick的原因）`
2. 将整个序列的信息压缩在了一个语义编码C中，用一个语义编码C来记录整个序列的信息，序列较短还行，如果序列是长序列，比如是一篇上万字的文章，我们要生成摘要，那么只是用一个语义编码C来表示整个序列的信息肯定会损失很多信息，而且序列一长，就可能出现梯度消失问题，这样将所有信息压缩在一个C里面显然不合理

## Attention

视觉注意力机制是人类视觉所特有的大脑信号处理机制。人类视觉通过快速扫描全局图像，获得需要重点关注的目标区域，也就是一般所说的注意力焦点，而后对这一区域投入更多注意力资源，以获取更多所需要关注目标的细节信息，而抑制其他无用信息。

同一张图片，不同的人观察注意到的可能是不同的地方，这就是人的注意力机制。attention 就是模仿人的注意力机制设计的。**深度学习中的注意力机制从本质上讲和人类的选择性视觉注意力机制类似，核心目标也是从众多信息中选择出对当前任务目标更关键的信息**

目前大多数注意力模型附着在Encoder-Decoder框架下，当然，其实注意力模型可以看作一种通用的思想，本身并不依赖于特定框架

### 优点：

* 速度快。`Attention机制不再依赖于RNN，解决了RNN不能并行计算的问题。`这里需要说明一下，基于`Attention`机制的 `seq2seq` 模型，是`有监督的训练`，所以在训练的时候，在`decoder`阶段并不是说预测出了一个词，然后再把这个词作为下一个输入，因为有监督训练，已经有了`target`的数据，所以是可以`并行输入`的，可以`并行计算decoder的每一个输出`，但是再做预测的时候，是没有`target`数据的，这个时候就需要基于上一个时间节点的预测值来当做下一个时间节点`decoder`的输入。所以节省的是`训练的时间`。
* 效果好。效果好主要就是因为注意力机制，能够获取到局部的重要信息，能够抓住重点。

### 缺点：

* 只能在`Decoder阶段实现并行运算`，`Encoder`部分依旧采用的是`RNN`，`LSTM` 这些按照`顺序编码`的模型，`Encoder`部分无法实现并行运算。
* 因为Encoder部分目前仍旧依赖于RNN，所以对于中长距离之间，`两个词相互之间的关系没有办法很好的获取`。

## Self-attention


在一般任务的 Encoder-Decoder 框架中，输入 Source 和输出 Target 内容是不一样的，比如对于英-中机器翻译来说，Source是英文句子，Target是对应的翻译出的中文句子，`Attention机制发生在Target的元素和Source中的所有元素之间`。而Self Attention顾名思义，指的不是Target和Source之间的Attention机制，而是Source内部元素之间或者Target内部元素之间发生的Attention机制，也可以理解为Target=Source这种特殊情况下的注意力计算机制。其具体计算过程是一样的，只是计算对象发生了变化而已。

引入 `Self Attention 后会更容易捕获句子中长距离的相互依赖的特征`，因为如果是 `RNN` 或者 `LSTM`，需要依次序序列计算，对于远距离的相互依赖的特征，要经过若干时间步步骤的信息累积才能将两者联系起来，而距离越远，有效捕获的可能性越小。但是**Self Attention在计算过程中会直接将句子中任意两个单词的联系通过一个计算步骤直接联系起来**，所以远距离依赖特征之间的距离被极大缩短，有利于有效地利用这些特征。除此外，Self Attention对于增加计算的并行性也有直接帮助作用。正好弥补了attention机制的两个缺点。
