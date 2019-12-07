import matplotlib.pyplot as plt
import numpy as np

n = np.arange(0,99)
if n.all() <= 9:
    f = n**2 - 7
else:
    f = n**2 - 7 - 10

plt.stem(n,f,'m')
plt.grid()
plt.show()
        

        