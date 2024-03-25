import numpy as np
import pandas as pd

data = np.random.randn(4, 3)

dataFrame = pd.DataFrame(data)

newDataFrame = pd.DataFrame(
    data,
    index=["Mertcan", "Sueda", "Göktuğ", "Gökçe"],
    columns=["Maaş", "Yaş", "Çalışma Saati"],
)

newDataFrame["Emeklilik Yaşı"] = newDataFrame["Yaş"] + newDataFrame["Yaş"]

# newDataFrame = newDataFrame.drop("Maaş", axis = 1)

newDataFrame.drop("Maaş", axis=1, inplace=True)

print(newDataFrame[newDataFrame < 0])

print(newDataFrame)

print(newDataFrame[newDataFrame["Emeklilik Yaşı"] > 0])
