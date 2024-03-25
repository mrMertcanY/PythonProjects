import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sbn
import tensorflow as tf
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential, load_model

dataFrame = pd.read_excel("bisiklet_fiyatlari.xlsx")

# sbn.pairplot(dataFrame)

# plt.show()

# y = wx + b
# y -> label
y = dataFrame["Fiyat"].values

# x -> feature (özellik)
x = dataFrame[["BisikletOzellik1", "BisikletOzellik2"]].values


x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=15
)


# scaling

scaler = MinMaxScaler()
scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

model = Sequential()

model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))

model.add(Dense(1))

model.compile(optimizer="rmsprop", loss="mse")

model.fit(x_train, y_train, epochs=250)

loss = model.history.history["loss"]

trainLoss = model.evaluate(x_train, y_train, verbose=0)
testLoss = model.evaluate(x_train, y_train, verbose=0)

testTahminleri = model.predict(x_test)

tahminDf = pd.DataFrame(y_test, columns=["Gerçek Y"])

testTahminleri = pd.Series(
    testTahminleri.reshape(
        330,
    )
)

tahminDf = pd.concat([tahminDf, testTahminleri], axis=1)
tahminDf.columns = ["Gerçek Y", "Tahmin Y"]

print(mean_absolute_error(tahminDf["Gerçek Y"], tahminDf["Tahmin Y"]))
print(mean_squared_error(tahminDf["Gerçek Y"], tahminDf["Tahmin Y"]))

yeniBisikletOzellikleri = [[1753, 1751]]

yeniBisikletOzellikleri = scaler.transform(yeniBisikletOzellikleri)

print(model.predict(yeniBisikletOzellikleri))

model.save("bisiklet_modeli.h5")

sonradancagirilanmodel = load_model("bisiklet_modeli.h5")

sbn.scatterplot(x="Gerçek Y", y="Tahmin Y", data=tahminDf)

# sbn.lineplot(x=range(len(loss)), y=loss)

# print(model.evaluate(x_train, y_train))

plt.show()
