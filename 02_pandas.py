# Data Cleaning -> Dealing with NULL Entity

# Deleting rows with NULL entity
import pandas as pd
df = pd.read_csv("https://github.com/YBI-Foundation/Dataset/raw/main/Titanic.csv")
df.info()
df = df.dropna()     # Remove rows with NULL entity
df.info()

# Replacing NULL entity with a value
df = pd.read_csv("https://github.com/YBI-Foundation/Dataset/raw/main/Titanic.csv")
df.info()
df["age"].fillna(df["age"].mean(),inplace=True)   # Replace NULL entity with mean
print(df["age"].head())


# Access or Replace a particular identity
df.loc[3,"age"] =40
df["age"].head()  