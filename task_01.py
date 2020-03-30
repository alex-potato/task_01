
import math
import matplotlib.pyplot as plt
import numpy as np
import os

A=0
x=-10


#os.remove('results1/task_01_4o-506c_Shemshura_09.txt')
#os.rmdir("results1")



if not os.path.isdir("results1"):
  path="results1"
  os.mkdir(path)
fp = open('results1/task_01_4o-506c_Shemshura_09.txt', 'w',encoding = 'utf-8')
x=np.linspace(-10,10,100)
f=0.5+(((np.sin(x**2-A**2))*(np.sin(x**2-A**2))-0.5) / ((1+0.001*(x**2+A**2))**2))
for i in range(21):
        print(x[i], ''*6, f[i], file=fp, end="\n")

print(x,"    ",f)
fp.close()
plt.figure()
plt.xlabel("x")         # ось абсцисс
plt.ylabel("f(x)")      # ось ординат
plt.plot(x,f)
plt.grid()
plt.savefig('image.png')            # включение отображение сетки
plt.show()
