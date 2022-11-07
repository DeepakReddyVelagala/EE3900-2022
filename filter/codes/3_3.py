import numpy as np
import matplotlib.pyplot as plt

X = np.array([1.0,2.0,3.0,4.0,2.0,1.0])

Y = np.loadtxt("codes/data.dat",dtype = np.double)
print(Y)

plt.subplot(2,1,1)
plt.stem(range(0,6),X)
plt.xlabel('$n$')
plt.ylabel('$X(n)$')

plt.subplot(2,1,2)
plt.stem(range(0,19),Y)
plt.xlabel('$n$')
plt.ylabel('$Y(n)$')

plt.grid()
plt.show()