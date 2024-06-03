import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


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
            # print(x)
            break
        
        i=0
        y=[]
        for row in spamreader:
            values = ','.join(row)
            values = values.split(",")
            y.append(float(values[0]))
            # print(y)
with open('resources/BMI_Age_2DFraminghamOLAPCube_dataset.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        z=[]
        i=0
        for row in spamreader:
         v=[]
         if i!=0:
            values = ','.join(row)
            values = values.split(",")
            values.pop(0)
            v= [float(value) if value != "" else np.NaN for value in values]
            z.append(v)
         i=1








X, Y = np.meshgrid(x, y)
# Z = np.sin(np.sqrt(X+ Y))




plt.figure()
contour = plt.contour(X, Y, z,  colors=['red', 'green', 'blue'], linestyles=['-', '--'])
plt.clabel(contour, inline=True, fontsize=8)
plt.xlabel('age')
plt.ylabel('bmi')
plt.grid(True)
plt.show()




# # Creating a 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Plotting the 3D contour
# ax.contour3D(X, Y, z, 50, cmap='plasma')

# # Adding contour lines on the XY plane
# ax.contour(X, Y, z, zdir='z', offset=np.min(z), cmap='plasma')

# # Customizing the plot
# ax.set_xlabel('X-Age')
# ax.set_ylabel('Y-BMI')
# ax.set_zlabel('Z-HeartRate')
# ax.set_title('3D Contour Plot with Contour Lines')

# # Displaying the plot
# plt.show()