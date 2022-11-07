import numpy as np
import matplotlib.pyplot as plt

N = 14

x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
nx = len(x)

x=np.pad(x, (0,8), 'constant', constant_values=(0))

k = np.arange(N)

# Z = np.linspace(0,2*np.pi*k,N+1) #z[i][j] such that i<k & j<N.
# print(Z/np.pi)

X = np.zeros(N)+ 1j*np.zeros(N)
for i in range(N):
    for j in range(N):
        X[i] += + x[j] * np.exp((1j*2*np.pi*i*j)/N)

# print(X) 

n = np.arange(N)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2
# plt.stem(np.arange(12), hn1+hn2)

H=np.zeros(N)+ 1j*np.zeros(N)

for i in range(N):
    for j in range(N):
        H[i] += h[j] * np.exp((1j*2*np.pi*i*j)/N)

Y = np.zeros(N)+1j*np.zeros(N)
for i in range(N):
    Y[i] = X[i]*H[i]

# plt.subplot(2,1,2)
plt.stem(range(0,N),Y)
plt.xlabel('$k$')
plt.ylabel('$Y(k)$')
plt.grid()

plt.show()