<!--
 * @Author: matiastang
 * @Date: 2021-12-15 11:39:23
 * @LastEditors: matiastang
 * @LastEditTime: 2022-08-04 11:13:16
 * @FilePath: /matias-AI/md/RNN循环神经网络.md
 * @Description: 循环神经网络
-->
# 循环神经网络

[LSTM和GRU的解析从未如此通俗易懂（动图）](http://www.360doc.com/content/19/0330/20/7669533_825345291.shtml)

## 循环神经网络的发展简史
循环神经网络（RNN，Recurrent Neural Network）的历史可以简单概括如下：

1933年，西班牙神经生物学家Rafael Lorente de Nó发现大脑皮层（cerebral cortex）的解剖结构允许刺激在神经回路中循环传递，并由此提出反响回路假设（reverberating circuit hypothesis）。
1982年，美国学者John Hopfield使用二元节点建立了具有结合存储（content-addressable memory）能力的神经网络，即Hopfield神经网络。
1986年，Michael I. Jordan基于Hopfield网络的结合存储概念，在分布式并行处理（parallel distributed processing）理论下建立了新的循环神经网络，即Jordan网络。
1990年，Jeffrey Elman提出了第一个全连接的循环神经网络，Elman网络。Jordan网络和Elman网络是最早出现的面向序列数据的循环神经网络，由于二者都从单层前馈神经网络出发构建递归连接，因此也被称为简单循环网络（Simple Recurrent Network, SRN）。
1990年，Paul Werbos提出了循环神经网络的随时间反向传播（BP Through Time，BPTT），BPTT被沿用至今，是循环神经网络进行学习的主要方法。
1991年，Sepp Hochreiter发现了循环神经网络的长期依赖问题（long-term dependencies problem），大量优化理论得到引入并衍生出许多改进算法，包括神经历史压缩器（Neural History Compressor, NHC）、长短期记忆网络（Long Short-Term Memory networks, LSTM）、门控循环单元网络（Gated Recurrent Unit networks, GRU）、回声状态网络（echo state network）、独立循环神经网络（Independent RNN）等。