<!--
 * @Author: matiastang
 * @Date: 2022-08-03 17:56:17
 * @LastEditors: matiastang
 * @LastEditTime: 2022-08-05 15:04:16
 * @FilePath: /matias-AI/md/self-attention.md
 * @Description: self-attention
-->
# self-attention

[self-attention](https://jalammar.github.io/illustrated-transformer/)
[自注意力(self-attention)](https://zhuanlan.zhihu.com/p/449028081)
[transformer](https://arxiv.org/pdf/1706.03762.pdf)
[重要-超详细图解Self-Attention的那些事儿](https://mp.weixin.qq.com/s?__biz=MzI5MDUyMDIxNA==&mid=2247579430&idx=1&sn=3c63a42410e2107f1f91f861dc25c3cb&scene=21#wechat_redirect)
[从零实现了Transformer模型](https://mp.weixin.qq.com/s?__biz=MzI5MDUyMDIxNA==&mid=2247578799&idx=1&sn=9f8fdb2718129e60559f4803a5682296&chksm=ec1d5956db6ad040fd77a8cd24fd2512d5a04ba422de670c49348a6a06fd70013fab14a1b750&scene=21#wechat_redirect)

`CNN`不能直接用于`处理变长的序列`样本但可以实现`并行计算`。完全基于CNN的Seq2Seq模型虽然可以并行实现，但非常占内存，很多的trick，大数据量上参数调整并不容易。【长期依赖问题&调参问题】

Self-Attention允许对依赖关系建模，而不需要考虑它们在输入或输出序列中的距离，并且可以将一个序列的不同位置串联起来。

## 多头注意力（multi headed self attention）

通过添加一种称为“多头”注意力的机制进一步完善了自注意力层。这通过两种方式提高了注意力层的性能：

1. 它扩展了模型关注不同位置的能力。是的，在上面的示例中，z1 包含一点其他编码，但它可能由实际单词本身主导。如果我们要翻译“动物因为太累而没有过马路”这样的句子，那么知道“它”指的是哪个词会很有用。

2. 它为注意力层提供了多个“表示子空间”。正如我们接下来将看到的，通过多头注意力，我们不仅有一个，而且还有多组查询/键/值权重矩阵（`Transformer 使用八个注意力头，因此每个编码器/解码器最终有八个集合`） . 这些集合中的每一个都是随机初始化的。然后，在训练之后，每个集合用于将输入嵌入（或来自较低编码器/解码器的向量）投影到不同的表示子空间中。

如果我们进行与上述相同的自注意力计算，只是使用不同的权重矩阵进行八次不同的计算，我们最终会得到八个不同的 Z 矩阵
![transformer_multi-headed_self-attention-recap](../md/images/transformer_multi-headed_self-attention-recap.png)

## 位置编码向量

这个常数8是键向量的维度的开方，键向量和查询向量的维度都是64，开方后是8。做这个尺度上的调整目的是为了易于训练。

## 残差

![transformer_resideual_layer_norm_2](..images/transformer_resideual_layer_norm_2.png)

这也适用于解码器的子层。如果我们想一个由 2 个堆叠编码器和解码器组成的 Transformer，它看起来像这样：

![transformer_resideual_layer_norm_3](..images/transformer_resideual_layer_norm_3.png)