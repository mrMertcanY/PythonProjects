import numpy as np

myList = [[10, 20, 30], [20, 30, 40], [40, 50, 60]]

myMatrixArray = np.array(myList)

# print(myMatrixArray[1, 2])

# print(myMatrixArray[1:, 2])  # 1. rowdan başlayıp 2. indexlerini getirir


newList = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24],
]


newMatrix = np.array(newList)

print(newMatrix[[0, 2, 4]])  # 0,2 ve 4. indexleri getirir
