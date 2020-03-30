
import matplotlib.pyplot as plt
import numpy as np
import os

A = 0

if not os.path.isdir("results"):
    path = "results"
    os.mkdir(path)

fp = open('results/task_01_4o-506c_Shemshura_09.txt', 'w', encoding='utf-8')
x = np.linspace(-10, 10, 500)
f = 0.5 + (((np.sin(x**2 - A**2)) * (np.sin(x**2 - A**2)) - 0.5) /
           ((1 + 0.001 * (x**2 + A**2))**2))
for i in range(21):
    print(x[i], '   ', f[i], file=fp, end="\n")

print(x, "    ", f)
fp.close()
plt.figure()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, f)
plt.grid()
plt.savefig('image.png')
plt.show()
