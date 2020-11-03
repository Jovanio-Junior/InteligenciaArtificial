import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([[1,5,118],
              [1,13,132],
              [1,20,119],
              [1,28,153],
              [1,41,91],
              [1,49,118],
              [1,61,132],
              [1,62,105]])
y = np.array([[8.1],
              [6.8],
              [7.0],
              [7.4],
              [7.7],
              [7.5],
              [7.6],
              [8.0]])

#print(x)
xtran = np.transpose(x)
#print(xtran)

xtran_x_x = np.mat(xtran) * np.mat(x)
#print(xtran_x_x)

xinv = np.linalg.inv(xtran_x_x)
#print(xinv)

xtran_x_y = np.mat(xtran) * np.mat(y)
#print(xtran_x_y)

xtran_x_x_xtran_x_y = np.mat(xinv) * np.mat(xtran_x_y)
#print(xtran_x_x_xtran_x_y)

aux = np.dot(x,xtran_x_x_xtran_x_y)
print(aux)