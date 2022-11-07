from turtle import color
import matplotlib .pyplot as plt
import numpy as np

y1 = np.loadtxt("codes/data.dat",dtype = np.double)


N = 14
n = np.arange(N)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2

xtemp=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
x=np.pad(xtemp, (0,8), 'constant', constant_values=(0))

X = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		X[k]+=x[n]*np.exp(-1j*2*np.pi*n*k/N)
H = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		H[k]+=h[n]*np.exp(-1j*2*np.pi*n*k/N)

Y = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	Y[k] = X[k]*H[k]

y2 = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		y2[k]+=Y[n]*np.exp(1j*2*np.pi*n*k/N)

#print(X)
y2 = np.real(y2)/N

# plt.stem(range(0,19),y1,label='sin')
# plt.setp('blue', plt.getp(markerline,'blue'))
# # plt.setp(stemlines, 'linestyle', 'dotted')

# plt.stem(range(0,N),y2,label = 'cos')
# plt.setp('red', plt.getp(markerline,'red'))
# # plt.setp(stemlines, 'linestyle', 'dotted')

# plt.title('Filter Output using DFT')
# plt.xlabel('$n$')
# plt.ylabel('$y(n)$')
# plt.grid()
# plt.show()

plt.stem(range(0,19),y1, 'b', markerfmt='go', label='y1')
plt.stem(range(0,N),y2, 'g', markerfmt='bo', label='y2')
plt.legend()
plt.grid()
plt.show()
