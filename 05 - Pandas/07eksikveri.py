import numpy as np
import pandas as pd

# dictionaryData = {
#     "İstanbul": [30, 29, np.nan],
#     "Ankara": [20, np.nan, 25],
#     "İzmir": [40, 39, 38],
# }

# weatherDataFrame = pd.DataFrame(dictionaryData)

# weatherDataFrameNA = weatherDataFrame.dropna(axis = 1)

# print(weatherDataFrameNA)

dictionaryData = {
    "İstanbul": [30, 29, np.nan],
    "Ankara": [20, np.nan, 25],
    "İzmir": [40, 39, 38],
    "Antalya": [45, np.nan, np.nan],
}

weatherDataFrame = pd.DataFrame(dictionaryData)

print(weatherDataFrame.dropna(axis=1, thresh = 2))

print(weatherDataFrame.fillna(20))