<!--
 * @Author: matiastang
 * @Date: 2022-08-03 17:56:17
 * @LastEditors: matiastang
 * @LastEditTime: 2022-08-04 17:52:54
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
