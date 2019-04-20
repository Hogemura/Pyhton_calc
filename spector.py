import math
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

h = 6.626*10**(-34)
c = 3*10**8
k = 1.38*10**(-23)
l = 2
while l<6:
    T = 1000*l

    x = np.arange(10**(-12), 6*10**(-6),10**(-12))
    y = (h*c**2/x**5)/(2.718**(h*c/(x*k*T))-1)

    plt.plot(x,y)
    l=l+1
plt.xlim(-0.5*10**(-6), 7*10**(-6))
plt.ylim(0, 0.75*10**(13))
plt.xticks([0.000002,0.000004,0.000006], ["2","4","6"])
plt.show()
