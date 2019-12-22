import pandas as pd
from pandas import DataFrame,Series
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv('StudentsPerformance.csv')

print(data.head(5))

print(data.describe())

data=data.drop(['lunch','test preparation course'],axis=1)

print(data)

data['parental level of education']=data['parental level of education'].fillna('School')

print(data['parental level of education'])

sb.countplot(x='gender',hue='test preparation course',data=data)
plt.show()