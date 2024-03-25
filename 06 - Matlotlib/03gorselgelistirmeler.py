import matplotlib.pyplot as plt
import numpy as np

npArray1 = np.linspace(0, 20, 20)

npArray2 = npArray1**3


newFigure = plt.figure()  # figsize=(6, 6), dpi=100

newAxes = newFigure.add_axes([0.1, 0.1, 0.9, 0.9])

newAxes.plot(npArray1, npArray1**2, label="npArray ** 2")
newAxes.plot(npArray1, npArray1**3, label="npArray ** 3")
newAxes.legend(loc=2)

newFigure.savefig("myFigure.png", dpi=1080)

plt.show()
