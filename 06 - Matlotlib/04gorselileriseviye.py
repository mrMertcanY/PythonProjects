import matplotlib.pyplot as plt
import numpy as np

numpyArray1 = np.linspace(0, 10, 20)

numpyArray2 = numpyArray1**2


(myFigure, myAxes) = plt.subplots()

myAxes.plot(numpyArray1, numpyArray2, "g", alpha=0.3)
myAxes.plot(numpyArray2, numpyArray1, color="#e84118")

(newFigure, newAxes) = plt.subplots()

newAxes.plot(numpyArray1, numpyArray1 + 2, color="blue", linewidth=8.0)
newAxes.plot(numpyArray1, numpyArray1 + 3, color="yellow", linewidth=6.0)
newAxes.plot(numpyArray1, numpyArray1 + 4, color="#e84118", linestyle="-.")
newAxes.plot(numpyArray1, numpyArray1 + 5, color="#e84118", linestyle=":")
newAxes.plot(numpyArray1, numpyArray1 + 6, color="#e84118", linestyle="--")

newAxes.plot(
    numpyArray1,
    numpyArray1 + 7,
    color="#000000",
    linestyle="--",
    marker="o",
    markersize=8,
    markerfacecolor="red",
)

newAxes.plot(
    numpyArray1,
    numpyArray1 + 8,
    color="#000000",
    linestyle="--",
    marker="+",
    markersize=4,
    markerfacecolor="red",
)

plt.show()
