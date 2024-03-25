import numpy as np
import pandas as pd

firstIndexes = [
    "Simpson",
    "Simpson",
    "Simpson",
    "South Park",
    "South Park",
    "South Park",
]

secondIndexes = ["Homer", "Bart", "Marge", "Cartman", "Kenny", "Kyle"]

mergeIndex = list(zip(firstIndexes, secondIndexes))

mergeIndex = pd.MultiIndex.from_tuples(mergeIndex)

myCartoonList = [[40, "A"], [10, "B"], [30, "C"], [9, "D"], [10, "E"], [11, "F"]]

cartoonNumpyArray = np.array(myCartoonList)

cartoonDataFrame = pd.DataFrame(
    cartoonNumpyArray, index=mergeIndex, columns=["Yaş", "Meslek"]
)
cartoonDataFrame.index.names = ["Film Adı", "İsim"]
print(cartoonDataFrame)
print(cartoonDataFrame.loc["Simpson"])
