import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
a = np.array([1,0])
b = np.array([2,1])
c = np.array([0,2])
x, y = np.meshgrid(a, b)
u = [0] * len(a)
v = [0] * len(a)
s, t = zip(*[a, b])
print(x,y)
print(s, t)
e = np.array(s)
f = np.array(t)

ax.quiver(u, v, s, t)
fig.savefig("justice.png")
plt.show()

