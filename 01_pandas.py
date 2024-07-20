import pandas as pd
df = pd.read_csv("https://github.com/YBI-Foundation/Dataset/raw/main/Titanic.csv")
print(df)
print(df.head())
print(df.info())
print(df.describe())
