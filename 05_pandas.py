# Removing Duplicates

import pandas as pd
data = {
    'Name': ['John', 'Anna', 'John', 'Anna', 'John'],
    'Age': [28, 24, 29, 24, 19],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

print(df.duplicated())           #Checking for duplicates
df1 = df.drop_duplicates()       #Removing duplicates
print(df)
print(df1)



# Removing data that has same email

data1 = {
    "Name":["a","b","c"],
    "email":["a@gmail.com","b@gmail.com","a@gmail.com"]
}
df2 = pd.DataFrame(data1)
print(df2)

print(df2.duplicated(subset="email"))
df2 = df2.drop_duplicates(subset="email", keep="last")   #keeping the last duplicate
print(df2)