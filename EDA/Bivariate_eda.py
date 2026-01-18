import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt

titanic= pd.read_csv('EDA/train.csv')
tips=sns.load_dataset('tips')
flights=sns.load_dataset('flights')
iris=sns.load_dataset('iris')

# print(titanic.head())
# print(tips.head())
# print(flights.head())
# print(iris.head())

# Numerical _ Numerical
# sns.scatterplot(x=tips['total_bill'], y= tips['tip'], hue=tips['time'], style=tips['day']) 
#hue here means color-coded by category—it visually separates and colors the scatter points based on the
# 'time' column values (like Lunch vs Dinner) in the same plot.

# Categorical , numerical 
# sns.barplot(x=titanic['Pclass'], y=titanic['Fare'], hue=titanic['Embarked'],)

# sns.boxplot(x=titanic['Sex'],y= titanic['Age'], hue=titanic['Survived'])

#  Numerical / categorical for single column distplot
# sns.displot(titanic[titanic['Survived']==0]['Age'], )
# sns.displot(titanic[titanic['Survived']==1]['Age'],)


sns.heatmap(pd.crosstab(titanic['Pclass'], titanic['Survived']))
# titanic.groupby('Pclass').mean()['Survived'] * 100 to calculate percentage 

sns.pairplot(iris)

plt.show()