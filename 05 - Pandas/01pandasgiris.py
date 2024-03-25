import numpy as np
import pandas as pd

# Seriler / Series

myDictionary = {
    "Mertcan": 21,
    "Sueda": 21,
    "Mehmet": 30,
}

print(pd.Series(myDictionary))


myAges = [50,40,30]

myNames = ["Atil","Zeynep","Mehmet"]

print(pd.Series(data = myAges,index = myNames))

numpyArray = np.array([50,40,30])

print(pd.Series(numpyArray, myNames))