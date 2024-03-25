import numpy as np
import pandas as pd

mergeDict1 = {
    "İsim": ["Göktuğ", "Gökçe", "Mertcan", "Sueda"],
    "Spor": ["Koşu", "Yüzme", "Koşu", "Basketbol"],
}

mergeDict2 = {
    "İsim": ["Göktuğ", "Gökçe", "Mertcan", "Sueda"],
    "Kalori": [100, 200, 150, 250],
}

mergeDataFrame1 = pd.DataFrame(mergeDict1)

mergeDataFrame2 = pd.DataFrame(mergeDict2)

mergeDataFrameFull = pd.merge(mergeDataFrame1, mergeDataFrame2, on="İsim")

print(mergeDataFrameFull)
