import pandas as pd


dataFrame = pd.read_excel("C:\PythonCodes\salary.xlsx")

fillvaluesDF = dataFrame.dropna()

fillvaluesDF.to_excel("C:\\PythonCodes\\newsalary.xlsx")

print(dataFrame)
