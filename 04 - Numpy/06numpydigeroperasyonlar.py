import numpy as np

newArray = np.random.randint(1, 100, 20)


print(newArray)

result = newArray > 24  # bunu newarray[result] gibi de kullanılabilir.

print(newArray[newArray > 24])


lastArray = np.arange(0,24)

print(lastArray + lastArray)

print(np.sqrt(lastArray))