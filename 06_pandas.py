#Pandas - Data Correlations

import pandas as pd 
data = {
    "Temperature": [22, 25, 32, 28, 30],
    "Ice_Cream_Sales": [105, 120, 135, 130, 125]
}
df = pd.DataFrame(data)
print(df.head())

print(df.info())
df.corr()

corr = df["Temperature"].corr(df["Ice_Cream_Sales"])          #when df has non numeric cols-> corr of whole df cant be calculated
print(corr)


#NOTE

'''
+ve corr ->Positive correlation refers to a relationship between two variables 
           where they both tend to change in the same direction. When one variable
           increases, the other variable also tends to increase, and when one variable
           decreases, the other variable also tends to decrease.

-ve corr ->Negative correlation, on the other hand, refers to a relationship between two
           variables where they tend to change in opposite directions. When one variable 
           increases, the other variable tends to decrease, and vice versa.
'''

# Correlation Methods

import spicy

pearson = df["Temperature"].corr(df["Ice_Cream_Sales"])                      #evaluates the linear relationship between two continuous variables
kendall = df["Temperature"].corr(df["Ice_Cream_Sales"], method='kendall')    #measures the ordinal association between two measured quantities
spearman = df["Temperature"].corr(df["Ice_Cream_Sales"], method='spearman')  #evaluates the monotonic relationship between two continuous or ordinal variables


print("pearson corr",pearson)
print("kendall corr",kendall)
print("spearman corr",spearman)


#NOTE

'''
Good Correlation-> A good correlation can range from 0.5 to 0.9 (positive or negative) 
                   and generally indicates a strong relationship between the variables

Bad Correlation-> A bad correlation is typically close to zero, indicating that there
                  is no relationship or any form of dependence between the two variables

Perfect Correlation-> +1 or -1 ; every increase/decrease in one variable, there is a
                      proportionate increase/decrease in the other variable.
'''