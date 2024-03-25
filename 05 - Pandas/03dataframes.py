import pandas as pd
import numpy as np


data = np.random.randn(4,3)

dataFrame = pd.DataFrame(data)

# print(dataFrame)

newDataFrame = pd.DataFrame(data, index = ["Mertcan", "Sueda", "Göktuğ", "Gökçe"], columns = ["Maaş", "Yaş", "Çalışma Saati"])

# print(newDataFrame[["Maaş","Yaş"]])

print(newDataFrame.loc["Mertcan"])

print(newDataFrame.iloc[1])
