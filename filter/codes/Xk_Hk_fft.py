import numpy as np
from scipy.fft import fft,ifft
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,2,1])
x=np.pad(x,(0,9),'constant',constant_values=(0))
N=15
def hn(n):
    if n<0:
        return 0
    if 0<=n<2:
       return (-1/2)**n
    else:
        return (-1/2)**n+(-1/2)**(n-2)
#computing the above using fft and ifft
xk1=fft(x)
htemp=np.array([hn(i) for i in range(N)])
hk1=fft(htemp)
yk1=xk1*hk1
yn1=ifft(yk1)
ntemp=np.array(list(range(N)))

plt.subplot(3,1,1)
plt.stem(range(0,N),xk1)
plt.ylabel('$X(n)$')
plt.grid()

plt.subplot(3,1,2)
plt.stem(range(0,N),hk1)
plt.ylabel('$H(n)$')
plt.grid()

plt.subplot(3,1,3)
plt.stem(ntemp,yk1)
plt.ylabel('$y(n)$')
plt.xlabel('$n$')
plt.grid()
plt.show()
