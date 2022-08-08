<!--
 * @Author: matiastang
 * @Date: 2021-12-15 11:39:04
 * @LastEditors: matiastang
 * @LastEditTime: 2022-08-08 16:35:47
 * @FilePath: /matias-AI/md/CNN/CNN卷积神经网络.md
 * @Description: CNN
-->
# CNN

![CNN可以看做是self-attention的特例](../md/images/CNN可以看做是self-attention的特例.png)

卷积神经网络（CNN，Convolutional Neural Net)是神经网络的类型之一，在图像识别和分类领域中取得了非常好的效果，比如识别人脸、物体、交通标识等，这就为机器人、自动驾驶等应用提供了坚实的技术基础。

一个典型的卷积神经网络中，会至少包含以下几个层：

* 卷积层
* 激活函数层
* 池化层
* 全连接分类层

经典的卷积神经网络模型

![卷积神经网络的鼻祖LeNet的模型结构](..../images/LeNet.png)

**1x1的卷积核关注的是不同通道的相同位置的像素之间的相关性，而不是同一通道内的像素的相关性，在本例中，意味着它关心的彩色通道信息，通过不同的卷积核，把彩色通道信息转变成另外一种表达方式，在保留原始信息的同时，还实现了降维。**

既然self-attention是更广义的CNN，则这个模型更加`flexible(灵活)`。而我们认为，一个模型越`flexible`，训练它所需要的数据量就越多，所以在训练`self-attention`模型时就需要更多的数据，这一点在论文 `ViT` 中有印证，它需要的数据集是有3亿张图片的私有数据集 `JFT-300`，性能超越了`CNN`。而如果不使用这么多数据而只使用`ImageNet`，则性能不如`CNN`。

Self-attention的attention map其实是随着样本的变化而不断变化的，所以从这个意义上它可以看做是instance-wise的一个网络。那么attention map与value矩阵作用就相当于是矩阵乘法，也就相当于是value通过一层FFN，只是这个FFN的参数是动态变化的。所以这个意义上也可以看做是一种更广义的CNN。