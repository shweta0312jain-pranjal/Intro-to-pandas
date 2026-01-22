import pandas as pd
import numpy as np

mydataset = {
    'cars' : ['BMW', 'Mercedes', 'Tesla'],
    'passings': [3, 7, 4]
}

df1 = pd.DataFrame(mydataset)
print(df1)

df = pd.DataFrame(mydataset, index=[1, 2, 3])
print(df)

print(df.iloc[0,[0,1]])
print(df.loc[1,['cars', 'passings']])

a = [1, 2, 3]
ser1 = pd.Series(a)
print(ser1)
ser = pd.Series([1, 2, 3], index= ['a', 'b', 'c'])
print(ser)
ser2 = pd.Series({"day1": 520, "day2": 390, "day3": 230})
print(ser2)

df2 = pd.read_csv("Countries Data.csv")
print(df2.head())
print(df2.info())
print("is null :", df.isnull().sum())
df2.dropna(inplace=True)
print("is null :", df.isnull().sum())
print(df2.head())