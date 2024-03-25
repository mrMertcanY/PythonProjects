import matplotlib.pyplot as plt
import numpy as np

numpyArray1 = np.linspace(0, 10, 20)

numpyArray2 = numpyArray1**2

# plt.scatter(numpyArray1, numpyArray2)

newArray = np.random.randint(0, 100, 50)


## HISTOGRAM

# plt.hist(newArray)

plt.boxplot(newArray)

plt.show()
