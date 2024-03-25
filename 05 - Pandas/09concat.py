import numpy as np
import pandas as pd

dict1 = {
    "Name": ["Ahmet", "Mehmet", "Mertcan", "Sueda"],
    "Spor": ["Koşu", "Yüzme", "Koşu", "Basketbol"],
    "Kalori": [100, 200, 300, 400],
}

dict2 = {
    "Name": ["Osman", "Levent", "Atlas", "Fatma"],
    "Spor": ["Koşu", "Yüzme", "Koşu", "Basketbol"],
    "Kalori": [200, 100, 50, 300],
}

dict3 = {
    "Name": ["Ayşe", "Mahmut", "Duygu", "Nur"],
    "Spor": ["Koşu", "Yüzme", "Badminton", "Tenis"],
    "Kalori": [300, 400, 500, 250],
}


dataFrame1 = pd.DataFrame(dict1)

dataFrame2 = pd.DataFrame(dict2)

dataFrame3 = pd.DataFrame(dict3)

dataFrameFull = pd.concat([dataFrame1, dataFrame2, dataFrame3]) #axis = 1 yapabiliyorum kolon birleştirmek için

print(dataFrameFull)
