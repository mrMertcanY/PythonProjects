import numpy as np
import pandas as pd

# print(pd.Series(["Mertcan", "Sueda", "Göktuğ"], [1, 2, 3]))

competetionResult1 = pd.Series([10, 5, 1], ["Mertcan", "Sueda", "Göktuğ"])

# print(competetionResult1)


competetionResult2 = pd.Series([20, 10, 8], ["Mertcan", "Sueda", "Göktuğ"])


print(competetionResult1 + competetionResult2)
