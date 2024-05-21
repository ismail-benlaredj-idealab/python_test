import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

from sys import path
path.append(r'C:\Program Files (x86)\Microsoft.NET\ADOMD.NET\150')

from pyadomd import Pyadomd



conn_str = 'Data Source=IDEALAB6; Initial Catalog=framingham_multidimensional_model'
query = """ 
WITH MEMBER [Measures].[AvgHeartRate] AS
CINT([Measures].[Heart Rate] / [Measures].[RowCount])

SELECT
  NON EMPTY { [Measures].[AvgHeartRate] } ON COLUMNS,
  NON EMPTY { ([Education].[Id Education].[Id Education],[Cigs Per Day].[Id Cigs Per Day].[Id Cigs Per Day]) } ON ROWS
FROM [Framingham];
"""

with Pyadomd(conn_str) as conn:
    with conn.cursor().execute(query) as cur:
         res= cur.fetchall()



for x in res:
   if None not in x and  "Unknown" not in x:
       print(x)
# Create axis
axes = [5, 5, 5]
 
# Create Data
data = np.ones(axes, dtype=np.bool_)
print(data)
# data = np.array(res)
# Control Transparency
alpha = 0.9
 
# Control colour
colors = np.empty(axes + [4], dtype=np.float32)
colors[0] = [1, 0, 0, alpha]  # red
colors[1] = [0, 1, 0, alpha]  # green
colors[2] = [0, 0, 1, alpha]  # blue
colors[3] = [1, 1, 0, alpha]  # yellow
colors[4] = [1, 1, 1, alpha]  # grey
 
# Plot figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
 
# Voxels is used to customizations of
# the sizes, positions and colors.
ax.voxels(data, facecolors=colors, edgecolors='grey')

plt.show() 



# WITH MEMBER [Measures].[AvgHeartRate] AS
# CINT([Measures].[Heart Rate] / [Measures].[RowCount])

# SELECT
#   NON EMPTY { [Measures].[AvgHeartRate] } ON COLUMNS,
#   NON EMPTY { ([Education].[Id Education].[Id Education],[Cigs Per Day].[Id Cigs Per Day].[Id Cigs Per Day]) } ON ROWS
# FROM [Framingham];


#   WITH MEMBER [Measures].[AvgHeartRate] AS
#   CINT([Measures].[Heart Rate] / [Measures].[RowCount])

# SELECT
#   NON EMPTY ( [Measures].[AvgHeartRate],[Gender].[Id Gender].[Id Gender] ) ON COLUMNS,
#   NON EMPTY { ([Education].[Id Education].[Id Education],[Cigs Per Day].[Id Cigs Per Day].[Id Cigs Per Day]) } ON ROWS
# FROM [Framingham];