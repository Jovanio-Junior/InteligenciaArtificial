import numpy as  np
import matplotlib.pyplot as plt

#criar uma base de dados aleatoria
rng = np.random.RandomState(0)
W = rng.randn(1000,2)
plt.scatter(W[:,0],W[:,1])
plt.axis('equal')
plt.grid('on')
A = rng.rand(2,2)
X = np.dot(W,A)

plt.scatter(X[:,0],X[:,1])
plt.axis('equal')
plt.grid('on')
np.var(X[:,0])
np.var(X[:,1])

C = np.cov(X.T)
e, V = np.linalg.eig(C)
V[:,0]
V[:,1]

u = V[:,1]

u.shape

Z = np.dot(X,u)
#Z.shape

np.dot(u,u)
Y=np.outer(Z,u)
plt.scatter(X[:,0], X[:,1])
plt.scatter(Y[:,0], Y[:,1])