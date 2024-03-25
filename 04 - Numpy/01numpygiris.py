import numpy as np

# Numpy Array


matrixList = [[10, 20, 30], [20, 30, 40], [30, 40, 50]]

print(np.array(matrixList))

# Arange

print(np.arange(0, 10, 2))

# Zeros & Ones

print(np.zeros((2, 2)))

print(np.ones(5))


# Linspace

print(
    np.linspace(0, 10, 20)
)  # Başlangıç index, Kaç'a kadar gidecek, Kaç tane eşit sayı olacak.


# Eye
print(
    np.eye(3)
)