import numpy as np
import pandas as pd

data = np.random.randn(4, 3)

dataFrame = pd.DataFrame(data)

newDataFrame = pd.DataFrame(
    data,
    index=["Mertcan", "Sueda", "Göktuğ", "Gökçe"],
    columns=["Maaş", "Yaş", "Çalışma Saati"],
)

newIndexList = list()

for item in newDataFrame.iloc:
    newIndexList.append(item.name[:3])



newDataFrame["Yeni Indeks"] = newIndexList

newDataFrame = newDataFrame.set_index("Yeni Indeks")

print(newDataFrame.loc["Mer"])
