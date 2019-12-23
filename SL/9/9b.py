import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sb

data=pd.read_csv('BlackFriday.csv')

print(data.head(5))
print(data.describe())

data['City_Category']=data['City_Category'].fillna('D')
print(data['City_Category'])

data['City_Category']=data['City_Category'].map({
    'A':'Metro Cities',
    'B':'Small Towns',
    'C':'Villages'
})

print(data['City_Category'])

sb.countplot(x='City_Category',data=data,hue='Gender')
plt.show()



