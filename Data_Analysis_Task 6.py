import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
data = pd.read_csv('heart.csv')

print(data.head())

data.tail()

data.columns.values

data.isna().sum()

data.info()

data.hist(bins=50,grid=False,figsize=(20,15))

data.describe()

questions=["1.how many people have heart disease and how manypeople doesn't have heart disease?",
"2.people of which sex has more heart disease?",
"3.people of which sex haswhich type of chest pain most",
"4.people with which chest painare most prone to have heart disesae"]

questions

data.output.value_counts()

data.output.value_counts().plot(kind='bar',color=["red","salmon"])
plt.title("Heart disease values")
plt.xlabel("1 = Heart disease ,0 = No heart disease")
plt.ylabel("Amount")

data.output.value_counts().plot(kind='pie',figsize=(8,6))
plt.legend({"Disease","No Disease"});

data.sex.value_counts()

pd.crosstab(data.output,data.sex)

sns.countplot(x='output',data=data,hue='sex')
plt.title("Heart disease frequency for sex ")
plt.xlabel("1 = Heart disease ,0 = No heart disease")

data.cp.value_counts

data.cp.value_counts().plot(kind='bar',color=['salmon','lightskyblue','khaki','springgreen'])
plt.title('chest pain type vs count');

pd.crosstab(data.sex,data.cp).plot(kind='bar',color=['salmon','lightskyblue','khaki','springgreen'])
plt.title('chest pain type vs count');

pd.crosstab(data.cp,data.output)

sns.countplot(x='cp',data=data,hue='output');

sns.displot(x='age',data=data,bins =30,kde='True');

sns.displot(x='thalachh',data=data,bins =30,kde='True',color='red');
