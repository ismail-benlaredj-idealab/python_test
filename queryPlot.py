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
  NON EMPTY ( [Measures].[AvgHeartRate],[Gender].[Id Gender].[Id Gender] ) ON COLUMNS,
  NON EMPTY { ([Education].[Id Education].[Id Education],[Cigs Per Day].[Id Cigs Per Day].[Id Cigs Per Day]) } ON ROWS
FROM [Framingham];
"""

with Pyadomd(conn_str) as conn:
    with conn.cursor().execute(query) as cur:
         res= cur.fetchall()
        #  print(res)


for x in res:
   if None not in x and  "Unknown" not in x:
      X, Y, Z =

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import axes3d

ax = plt.figure().add_subplot(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)

# Plot the 3D surface
ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8,
                alpha=0.3)

# Plot projections of the contours for each dimension.  By choosing offsets
# that match the appropriate axes limits, the projected contours will sit on
# the 'walls' of the graph.
ax.contour(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')

ax.set(xlim=(-40, 40), ylim=(-40, 40), zlim=(-100, 100),
       xlabel='X', ylabel='Y', zlabel='Z')
ax.set(xlim=(-80, 80), ylim=(-80, 80), zlim=(-80, 80),
       xlabel='X', ylabel='Y', zlabel='Z')

plt.show()