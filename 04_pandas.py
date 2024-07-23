# # Fixing wrong data

import pandas as pd
data = {
    'Name': ['John', 'Michael', 'Tom', 'Alex', 'Ryan'],
    'Age': [8, 9, 7, 80, 100],
    'Gender': ['M', 'M', 'M', 'F', 'M'],
    'Standard': [3, 4, 12, 3, 5]
}

df = pd.DataFrame(data)
print(df)
df.loc[3,"Gender"]='M'        #Fixing individual data
print(df)


u=[]
for i in df.index:            #Fixing  values with condition
    age_val = df["Age"]
    if(age_val[i]>15):
        u.append(i)
data1=df.copy()
print(data1)

data1 = data1.drop(u)
mean_=data1["Age"].mean()

for i in df.index:
    age_val = df["Age"]
    if(age_val[i]>15):
        df.loc[i,'Age'] = mean_

# print(df.index)
print("D",df)

# print("D1",data1)
# print(u)
# print("ageval",age_val)