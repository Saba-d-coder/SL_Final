import pandas as pd
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
import seaborn as sb

data=pd.read_csv('train.csv')

print(data.head(5))
print(data.describe())

data=data.drop(['SibSp','Parch'],axis=1)
print(data)

data['Cabin']=data['Cabin'].fillna('100')
print(data['Cabin'])

sb.countplot(x = 'Pclass', hue = 'Survived',data = data)
plt.show()