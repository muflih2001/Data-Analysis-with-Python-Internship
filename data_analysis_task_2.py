# -*- coding: utf-8 -*-
"""Data Analysis Task 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f7ZdlqMRn4kurNCxR0R6K7QMsPAFJ4SE
"""

import pandas as pd

data= pd.read_csv("winequality-red.csv")

data.info()

data.columns

data.head()

data.tail()

data.isnull()

data1=data.dropna()

data1

data2=data.fillna("Data yet to be Collected")

data.drop("chlorides",axis=1)

data.describe()

data.sum()

data.rename(columns={'free sulfur dioxide':'free sulphur dioxide'})

data.drop_duplicates()

q1 = data.quantile(0.25)
q3 = data.quantile(0.75)

print("Lower Quartile \n ", q1)
print("Upper Quartile \n", q3)

