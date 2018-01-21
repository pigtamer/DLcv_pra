"""
对cifar 10 的说明：
cifar10 数据集的所有图像都是在十个类别之中，32*32*3 尺寸。
其数据结构是字典，
1.字典的数据是10000x3072 nparray
2.字典的键是对应的标记
All images in cifar-10 are in 10 categories.
Size:32*32*3
Its container structrure is dictionary
data: 10000x3072 nparray, dtype = unit8.
      R 1024 + G 1024 + B 1024 = RGB 3072, 1024 = 32*32
      10000 images in total.
key: labels fr each image.
ref: https://www.cs.toronto.edu/~kriz/cifar.html
"""
###
import numpy as np
import cv2 as cv
import _pickle as pickle # on py3.x cPickle is changed to _pickle.

class load_cifar:
    def __init__(self):
        pass

    def unpickle(self, file):
        with open(file, 'rb') as fo:
            dict = pickle.load(fo, encoding='bytes')
        return dict

