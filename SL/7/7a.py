import pandas as pd
from pandas import DataFrame,Series
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv('iris.csv')

print(data.head(5))

print(data.describe())

data=data.drop([' Petal_Length'],axis=1)
print(data)

print("Average is:",data[[' Petal_Width','Class']].groupby('Class').mean())

sb.countplot(x=' Sepal_Width',hue='Class',data=data)
plt.show()