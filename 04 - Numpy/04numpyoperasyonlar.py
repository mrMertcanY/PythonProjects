import numpy as np


myArray = np.arange(0,15)

print(myArray[3:5]) # başlangıç index , bitiş index

myArray[3:8] = -5

# print(myArray)



otherArray = np.arange(0,24)

slicingArray = otherArray[4:9]

slicingArray[:] = 700

print(otherArray)


#### DİZİNİN ETKİLENMEMESİ İÇİN COPY KULLANILMALI !!!

sampleArray = np.arange(0,24)

sampleArrayCopy = sampleArray.copy()

sampleSlicingArray = sampleArrayCopy[4:9] 

sampleSlicingArray[:] = 700


print(sampleArray)