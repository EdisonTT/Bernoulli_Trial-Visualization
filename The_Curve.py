#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
 
# Dataset
x=np.array([0,1, 2, 3, 4, 5, 6, 7, 8,9,10])
y=np.array([0.00098, 0.00977, 0.04395, 0.11719, 0.20508, 0.24609, 0.20508, 0.11719, 0.04395, 0.00977, 0.00098])
 
cubic_interploation_model = interp1d(x, y, kind = "cubic")
 
# Plotting the Graph
X_=np.linspace(x.min(), x.max(), 500)
Y_=cubic_interploation_model(X_)
 
plt.plot(X_, Y_)
plt.title("The Normal Distribution Curve")
plt.xlabel("Number of times HEAD/TAIL obtained")
plt.ylabel("The Probability")
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()