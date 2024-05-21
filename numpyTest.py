import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



import csv

with open('resources/BMI_Age_2DFraminghamOLAPCube_dataset.csv', newline='') as csvfile:

    spamreader = csv.reader(csvfile)
    i=0
    for row in spamreader:
     values = ','.join(row)
     values = values.split(",")
     if i==0:
       values.pop(0)
     x = [float(value) if value!="" else None for value in values]
    #  print(x)
     break
  
    i=0
    y=[]
    for row in spamreader:
     values = ','.join(row)
     values = values.split(",")
     y.append(float(values[0]))
    # print(y)
    # z=[]
    # for row in spamreader:
    #  values = ','.join(row)
    #  values = values.split(",")
    #  if i!=0:
    #    z.append([float(value) if value!="" else None for value in values])
    # print(z)
print(y)
X, Y = np.meshgrid(x, y)

Z = np.exp(-0.0001 * ((X - 3000)**2 + (Y - 0)**2)) - np.exp(-0.0002 * ((X - 6000)**2 + (Y - 0)**2))
print(Z[0][0])
# levels = np.linspace(Z.min(), Z.max(), 10)


plt.figure()
contour = plt.contour(X, Y, Z,  colors=['red', 'green', 'blue'], linestyles=['-', '--'])
plt.clabel(contour, inline=True, fontsize=8)
plt.xlabel('age')
plt.ylabel('bmi')
plt.grid(True)
plt.show()

