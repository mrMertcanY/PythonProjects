import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sbn
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

dataFrame = pd.read_excel("merc.xlsx")


# print(sbn.distplot(dataFrame["price"]))
# print(dataFrame.corr(numeric_only=True)["price"].sort_values())

# print(dataFrame.sort_values("price", ascending=False).head(20))

# sbn.scatterplot(x="mileage", y="price", data=dataFrame)

percentNinetyNineDF = dataFrame.sort_values("price", ascending=False).iloc[131:]

dataFrame = percentNinetyNineDF
# print(dataFrame[dataFrame.year != 1970].groupby("year").mean("price")["price"])

dataFrame = dataFrame.drop("transmission", axis=1)

y = dataFrame["price"].values
x = dataFrame.drop("price", axis=1).values

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=10
)

scaler = MinMaxScaler()

x_train = scaler.fit_transform(x_train)

x_test = scaler.transform(x_test)

model = Sequential()

model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))

model.add(Dense(1))

model.compile(optimizer="adam", loss="mse")

model.fit(
    x=x_train, y=y_train, validation_data=(x_test, y_test), batch_size=250, epochs=300
)

guessArray = model.predict(x_test)

plt.scatter(y_test, guessArray)
plt.plot(y_test, y_test, "g-*")

print(dataFrame.iloc[2])

newCarSeries = dataFrame.drop("price", axis=1).iloc[2]

newCarSeries = scaler.transform(newCarSeries.values.reshape(-1, 5))

print(model.predict(newCarSeries))


print(mean_absolute_error(y_test, guessArray))

# lossValue = pd.DataFrame(model.history.history)

# lossValue.plot()

plt.show()
