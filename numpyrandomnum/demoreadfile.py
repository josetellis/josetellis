import numpy as np
import  matplotlib.pyplot as plt
num=np.fromfile("D://data/numbers.txt",dtype=int,sep=",")
items=np.genfromtxt("D:/data/items.txt",dtype='str',delimiter=",")
x=np.arange(len(items))
plt.bar(x,num)
plt.xticks(x,items)
plt.ylabel("Numbers")
plt.xlabel("Items")
plt.show()