import numpy as np
import pandas as pd

salaryDict = {
    "İsim": ["Mertcan", "Sueda", "Göktuğ", "Gökçe"],
    "Departman": ["Yazılım", "Satış", "Pazarlama", "Yazılım"],
    "Maaş": [200, 300, 400, 500],
}

salaryDataFrame = pd.DataFrame(salaryDict)

print(salaryDataFrame["Departman"].unique())

print(salaryDataFrame["Departman"].nunique())

print(salaryDataFrame["Departman"].value_counts())


def bruttenNete(salary):
    return salary * 0.66


print(salaryDataFrame["Maaş"].apply(bruttenNete))

print(salaryDataFrame.isnull())
