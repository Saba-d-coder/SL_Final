import pandas as pd
from pandas import DataFrame,Series
import seaborn as sb
import matplotlib.pyplot as plt

data=pd.read_csv('StudentsPerformance.csv')

print(data.head(5))

print(data.describe())

print(data.drop(['lunch','test preparation course'],axis=1))

data['parental level of education']=data['parental level of education'].fillna('School')

print(data['parental level of education'])

sb.countplot(x='gender',hue='test preparation course',data=data)
plt.show()