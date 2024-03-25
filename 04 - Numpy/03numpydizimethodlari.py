import numpy as np

myNumpyArray = np.arange(0, 30)

print(myNumpyArray.reshape(6, 5))

print(myNumpyArray.max())

print(myNumpyArray.min())

######################################

print(myNumpyArray.argmax())  # index verir

print(myNumpyArray.argmin())  # index verir


reshapeDizim = myNumpyArray.reshape(5, 6)

print(reshapeDizim.shape)
