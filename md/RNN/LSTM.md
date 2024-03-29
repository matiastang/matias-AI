<!--
 * @Author: matiastang
 * @Date: 2021-12-15 11:41:40
 * @LastEditors: matiastang
 * @LastEditTime: 2022-08-08 17:09:20
 * @FilePath: /matias-AI/md/RNN/LSTM.md
 * @Description: LSTM
-->
# LSTM

[LSTM和GRU的解析从未如此通俗易懂（动图）](http://www.360doc.com/content/19/0330/20/7669533_825345291.shtml)

`LSTM`设计了 `门控（gate）` 结构，控制信息的保留和丢弃。LSTM有三个门，分别是：`遗忘门（forget gate）`，`输入门（input gate）`和`输出门（output gate）`。

常见的LSTM结构

![LSTM内部结构意图](../images/lstm_inner_structure.png)

在解释完RNN之后，LSTM就比较好理解了，事实上，当文本很长的时候，本文中的例子只取了前200个单词进行分析，但当文本很长，神经元个数增多的时候，RNN就会出现弊端，它对于文本前后关系中"距离"比较近的关系能够比较好的表现出来，也就是短期记忆，这样对于长文本的效果就不那么好了，`LSTM`和`GRU`是解决`短期记忆`的方案。

它们具有称为门（gate）的内部机制，它可以调节信息流。这些门可以了解序列中哪些数据重要以进行保留或丢弃。这样，它可以将相关信息传递到长序列中进行预测。

LSTM只是在每个单元中加入了三个门控单元，分别是：

遗忘门：用来让RNN“忘记”之前没有用的信息。
更新门：用来让RNN决定当前输入数据中哪些信息将被留下来。
输出门：LSTM在得到最新节点状态c后，结合上一时刻节点的输y ( t − 1 ) y^{(t-1)}y 
(t−1)
  和当前时刻节点的输入x t x^tx 
t
 来决定当前时刻节点的输出。
具体的单元结构如下图所示