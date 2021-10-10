import matplotlib.pyplot as plt
import numpy as np

x_as = [10,9,8]
y_as = [10,9,8]


X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)
print(X)
fig, ax = plt.subplots()
q = ax.quiver(x_as, y_as, 1, 0)

#ax.quiverkey(q, X=0.3, Y=1.1, U=10, label='Quiver key, length = 10', labelpos='E')

plt.show()