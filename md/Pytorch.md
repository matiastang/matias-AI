<!--
 * @Author: matiastang
 * @Date: 2022-08-05 15:59:16
 * @LastEditors: matiastang
 * @LastEditTime: 2022-08-05 16:00:28
 * @FilePath: /matias-AI/md/Pytorch.md
 * @Description: Pytorch
-->
# Pytorch

![Pytorch]()

## Tensorflow的对比

这里我们还是和前面一样，实现一个隐层的全连接神经网络，优化的目标函数是预测值和真实值的欧氏距离。这个实现使用基本的Tensorflow操作来构建一个计算图，然后多次执行这个计算图来训练网络。**Tensorflow和PyTorch最大的区别之一就是`Tensorflow使用静态计算图`和`PyTorch使用动态计算图`**。在Tensorflow里，我们首先构建计算图，然后多次执行它。