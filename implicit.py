import math
import numpy as np
import matplotlib.pyplot as plt

pi = math.pi
a = 2/pi**2
l = 6
m = 100
n = 10
T = 5
h = l/n
tau = T/m
x = np.zeros(n+1)
t = np.zeros(m+1)
for i in range(n+1):
    x[i] = i*h
for k in range(m+1):
    t[k] = k*tau
gamma = ((a**2)*tau)/(h**2)
U = np.zeros((m+1, n+1))


def initialCondition(x):
    return math.sin(pi*x/2)


for i in range(n+1):
    U[0, i] = initialCondition(x[i])

for k in range(1, m+1):
    r = np.zeros(n-1)
    for i in range(0, n-1):
        r[i] = -U[k-1, i+1]-tau
    delta = np.zeros(n-1)
    lamb = np.zeros(n-1)
    b = gamma
    c = -1 - gamma
    d = gamma
    delta[0] = -d/c
    lamb[0] = r[0]/c
    for i in range(1, n-1):
        delta[i] = d/(c+b*delta[i-1])
        lamb[i] = (r[i] - b*lamb[i-1])/(c+b*delta[i-1])
    res = np.zeros(n-1)
    res[n-2] = lamb[n-2]
    for i in range(n-3, -1, -1):
        res[i] = delta[i]*res[i+1] + lamb[i]
    for i in range(1, n):
        U[k, i] = res[i-1]

for k in range(1, m+1):
    U[k, n] = t[k]

for k in range(1, m+1):
    U[k, 0] = U[k, 1] + h*t[k]

y0 = []
for k in range(0, m+1):
    y0 = []
    for i in range(0, n+1):
        y0.append(U[k, i])
    if ((t[k] == 0) or (t[k] == 0.2) or (t[k] == 0.4) or (t[k] == 0.6) or (t[k] == 0.8) or (t[k] == 1)):
        plt.plot(x, y0, label="t = %.1f" %t[k])

plt.title("Неявная схема")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend(loc=0)
plt.show()
