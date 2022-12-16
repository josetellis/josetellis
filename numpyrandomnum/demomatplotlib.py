import numpy as np
import  matplotlib.pyplot as plt
x=np.linspace(0,20,10)# Evenly spaced between  0 to 20
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,label="sine")
plt.plot(x,y2,label="cos")
plt.legend(loc="right")
plt.show()