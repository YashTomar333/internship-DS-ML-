# Reading a file and getting summary(information) about the columns

import pandas as pd
df = pd.read_csv("https://github.com/YBI-Foundation/Dataset/raw/main/Titanic.csv")
print(df)
print(df.head())
print(df.info())
print(df.describe())


# Minimuam rows that will display & Max Rows that will display

pd.options.display.min_rows = 10
print(df)
pd.options.display.max_rows = 60
print(df)


# Working with json file

df1 = pd.read_json("https://github.com/YBI-Foundation/Dataset/raw/main/Titanic.json")
print(df1)
print(df1.to_string())      # prints whole file
