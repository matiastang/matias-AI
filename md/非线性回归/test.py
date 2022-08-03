'''
Author: matiastang
Date: 2022-08-03 16:20:10
LastEditors: matiastang
LastEditTime: 2022-08-03 16:41:49
FilePath: /matias-AI/md/非线性回归/test.py
Description: 一元多项式
'''
#!/usr/bin/python3
#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 定义0-1之间的等距的10个点
    x = np.linspace(0, 1, 10)
    w = 1.1
    b = 0.2
    y = w * x + b
    line1 = plt.plot(x, y, marker='.')

    x2 = x * x
    w2 = -0.5
    y2 =  w * x + w2 * x2 + b
    line2 = plt.plot(x, y2, marker='s')

    x3 = x * x * x
    w3 = 2.3
    y3 =  w * x + w2 * x2 + w3 * x3 + b
    line3 = plt.plot(x, y3, marker='x')

    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("linear and non-linear")
    plt.legend([line1,line2,line3], ["x","x*x","x*x*x"])
    plt.show()