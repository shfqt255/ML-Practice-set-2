from sklearn import datasets
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 

data_frame=pd.read_csv('EDA/train.csv')

#it displays the probabillity
sb.distplot(data_frame['Age'])
# plt.show()

# It helps to how much the data is noisy
plt.boxplot(data_frame['Age'])
plt.show()

