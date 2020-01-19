from body import Body
from matplotlib import pyplot as plt 


b = Body(5, 1, 1)
dt = 0.001

for i in range(20):
    b.step(dt)
    b.plot()
plt.show()