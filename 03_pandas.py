# Cleaning data of wrong format

import pandas as pd


data = {
    'Country': ['USA', 'Canada', 'Australia', 'Germany', 'Japan'],
    'Date': ['2023-07-20', '2023-07-21', '2023-07-22', '2023-07-23', '2023-07-24'],
    'Temperature': [25.5, '28.0', 30.2, 22.8, 26.3]
    }

print(data)
df = pd.DataFrame(data)
print(df)
df["Temperature"].info             #for checking its datatype
df['Temperature'].astype(float)    #type casting to float


df1 = pd.DataFrame({'date': ['2022-12-01', '01/02/2022', '2022-03-23', '03/02/2022', '3 4 2023', '2023.9.30']})
df1["date"] = pd.to_datetime(df1["date"], format="mixed", dayfirst=True)   #Cleaning format for date
print(df1)
df1.info()