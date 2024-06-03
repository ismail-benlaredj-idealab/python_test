import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
framingham = pd.read_csv('resources/framingham.csv')
bins = [framingham['age'].min(), 40, 50, 60, framingham['age'].max()]
labels = ['Age < 40', '40 <= Age < 50', '50 <= Age < 60', 'Age >= 60']

# Discretize the 'age' column
framingham['AgeGroup'] = pd.cut(framingham['age'], bins=bins, labels=labels, right=False, include_lowest=True)

print(framingham)
# ******************************************************
pos = [] 
neg = [] 
grouped_data = framingham.groupby(['AgeGroup','TenYearCHD'])
column_name = 'AgeGroup'
for group_name, group_data in grouped_data:
    # print(f"*****************************: {group_name}")
    var= group_data[column_name]
    len=group_name.__len__()-2
    print(group_name[1])
    if group_name[1] == 0:
        pos.append(var.__len__())
    else:
        neg.append(var.__len__())

unique = framingham['AgeGroup'].unique()

# print(pos)
# print(neg)


unique=np.array(unique)
unique=unique[0:4]
print("**************************")
print(unique)
# X_axis = np.arange(len(unique)) 
X_axis =[0.0,1.0,2.0,3.0]
X_axis=np.array(X_axis)
plt.bar(X_axis-0.1, pos, 0.2, label = 'CHD') 
plt.bar(X_axis+0.1, neg, 0.2, label = 'NO CHD') 
  
plt.xticks(X_axis, unique) 
plt.xlabel("age") 
plt.ylabel("counts") 
plt.title("xx") 
plt.legend() 
plt.show() 


