import matplotlib.pyplot as plt
import numpy as np

ageList = [10, 20, 30, 30, 30, 40, 50, 60, 70, 75]

kgList = [20, 60, 80, 85, 86, 87, 70, 90, 95, 90]

numpyAgeList = np.array(ageList)

numpyKGList = np.array(kgList)

plt.plot(numpyAgeList, numpyKGList, "g") # "g" -> green

plt.xlabel("Yaş")
plt.ylabel("Kilo")
plt.title("Kilo'nun Yaşa Göre Değişim Grafiği")

plt.show()