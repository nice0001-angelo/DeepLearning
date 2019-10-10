import numpy as np

Data_set = np.loadtxt("../dataset/linearReg.csv", delimiter=",")

x = Data_set[:,0:1]
y = Data_set[:,1]

print(x)
