import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import seaborn as sns

# IMPORT LOWER LAYER
import load_cifar

class kNNClassfier:
    def __init__(self):
        pass

    def train(self, X, y): # for model training
        # x: N*D, each row is a example from cifar 10
        # this is the data structure of CIFAR
        self.Xtrain = X
        self.ytrain = y

    def pred(self, X):
        num_test = X.shape[0]
        Ypred = np.zeros(num_test, dtype=self.ytrain.dtype)
        for i in range(num_test):
            distance = np.sum(np.abs(self.Xtrain - X[i, :]), axis = 1)
            minidx = np.argmin(distance)
            Ypred = self.ytrain[minidx]
        return Ypred

file_path = "../dataset/cifar10/data_batch_"
file_idx = 1

FILE_NAME = file_path + str(file_idx)

images, labels = load_cifar.extractImagesAndLabels(FILE_NAME)
print(images.shape)
im1 = np.array(images[0])
print(im1.shape)

plt.imshow(im1)
plt.show()