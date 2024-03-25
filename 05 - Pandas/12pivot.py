import numpy as np
import pandas as pd

data = {
    "Karakter Sınıfı": ["South Park", "South Park", "Simpson", "Simpson", "Simpson"],
    "Karakter İsmi": ["Cartman", "Kenny", "Homer", "Bart", "Bart"],
    "Karakter Yaşı": [9, 10, 50, 20,10],
}


characterDF = pd.DataFrame(data)

print(
    characterDF.pivot_table(
        values="Karakter Yaşı", index=["Karakter Sınıfı", "Karakter İsmi"],
        aggfunc=np.sum
    )
)
