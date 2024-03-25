import numpy as np
import pandas as pd

salaryDictionary = {
    "Departman": [
        "Yazılım",
        "Yazılım",
        "Pazarlama",
        "Pazarlama",
        "İnsan Kaynakları",
        "İnsan Kaynakları",
    ],
    "Çalışan İsmi": ["Ahmet", "Mehmet", "Mertcan", "Sueda", "Göktuğ", "Gökçe"],
    "Maaş": [100, 150, 200, 300, 400, 500],
}

salaryDataFrame = pd.DataFrame(salaryDictionary)


groupObject = salaryDataFrame.groupby("Departman")

# print(groupObject.count())

# print(groupObject.mean("Maaş"))

# print(groupObject.min())

# print(groupObject.max())