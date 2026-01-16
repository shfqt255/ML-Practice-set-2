from sklearn import datasets
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 

# Deals with Categorical Data
data_frame=pd.read_csv('EDA/train.csv')
print(data_frame.head())

sb.countplot(data_frame['Sex'])
# data_frame['Embarked'].value_counts().plot(kind='bar'),
# # data_frame['Pclass'].value_counts().plot(kind='pie', autopct='% .2f')
plt.show()

# Deals With Numerical Data
# Histogram
plt.hist(data_frame['Age'], bins=50) # bins means how much bars you want to show. 
plt.show()