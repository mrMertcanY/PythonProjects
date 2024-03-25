import matplotlib.pyplot as plt
import numpy as np

npArray1 = np.linspace(0, 20, 20)

npArray2 = npArray1**3

# plt.plot(npArray1, npArray2, "g*-") # -- => çizgiler ekler *- => yıldızlarla gösterir

plt.subplot(1, 2, 1)  # 1 sıra , 2 kolon, 1. grafik
plt.plot(npArray1, npArray2, "r*-")

plt.subplot(1, 2, 2)  # 1 sıra , 2 kolon, 2. grafik
plt.plot(npArray2, npArray1, "g--")

myFigure = plt.figure()

figureAxes = myFigure.add_axes([0.1, 0.1, 0.3, 0.3])

figureAxes.plot(npArray1, npArray2, "g")
figureAxes.set_xlabel("X Ekseni Veri İsmi")
figureAxes.set_ylabel("Y Ekseni Veri İsmi")
figureAxes.set_title("Grafik Başlığı")

############################################################################

figure2 = plt.figure()

eksen1 = figure2.add_axes([0.1, 0.1, 0.9, 0.9])
eksen2 = figure2.add_axes([0.2, 0.5, 0.3, 0.3])

eksen1.plot(npArray1, npArray2, "g")
eksen1.set_xlabel("X Ekseni")
eksen1.set_ylabel("Y Ekseni")
eksen1.set_title("Ana Grafik Başlık")

eksen2.plot(npArray2, npArray1, "b")
eksen2.set_xlabel("Küçük X Ekseni")
eksen2.set_ylabel("Küçük Y Ekseni")
eksen2.set_title("Küçük Ana Grafik Başlık")

####################################################################

(myFG1, myAxes) = plt.subplots(nrows=1, ncols=2)


for axes in myAxes:
    axes.plot(npArray1, npArray2, "g")
    axes.set_xlabel("X Ekseni")

plt.tight_layout()

plt.show()
