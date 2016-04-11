import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import visvis as vv

def plot_flowgrid_dots(flowgrid):
    max_x, max_y, max_z = flowgrid.voxels.shape
    
    mx = -np.inf
    for x in range(max_x):
        for y in range(max_y):
            for z in range(max_z):
                v = flowgrid[x,y,z].get_total_access_counts()
                mx = max(mx, v)
         
    print(mx)
    
    plt.figure
    ax = plt.gca(projection='3d')
    for x in range(max_x):
        for y in range(max_y):
            for z in range(max_z):
                v = float(flowgrid[x,y,z].get_total_access_counts()) / mx
                color = plt.cm.spectral(v)
                ax.scatter([10*x], [10*y], [10*z], c=color, edgecolors=color, s=2)
    plt.show()
                

def plot_flowgrid_stack(flowgrid):
    max_x, max_y, max_z = flowgrid.voxels.shape
    
    mx = -np.inf
    for x in range(max_x):
        for y in range(max_y):
            for z in range(max_z):
                v = flowgrid[x,y,z].get_total_access_counts()
                mx = max(mx, v)
         
    print(mx) 
    
    X, Y = np.mgrid[:max_x, :max_y]
    Z    = np.ones((max_x, max_y), dtype=np.uint64)
    for z in range(max_z):
        data = np.zeros((max_x, max_y), dtype=np.float64)
        for x in range(max_x):
            for y in range(max_y):
                data[x,y] = float(flowgrid[x,y,z].get_total_access_counts()) / mx              
        vv.functions.surf(X, Y, Z*z*50, plt.cm.spectral(data), aa=3)
        
def plot_flowgrid(flowgrid):
    max_x, max_y, max_z = flowgrid.voxels.shape
    
    mx = -np.inf
    for x in range(max_x):
        for y in range(max_y):
            for z in range(max_z):
                v = flowgrid[x,y,z].get_total_access_counts()
                mx = max(mx, v)
         
    print(mx) 
    
    for z in range(max_z):
        data = np.zeros((max_x, max_y), dtype=np.float64)
        for x in range(max_x):
            for y in range(max_y):
                data[x,y] = float(flowgrid[x,y,z].get_total_access_counts()) / mx   
        
        colors = plt.cm.Greys(data)
        resized = cv2.resize(colors, (10*max_x, 10*max_y))           
        cv2.imshow(str(z), resized)
        cv2.waitKey(0)
  
# Usage:
#
#	from loader import load    
#	plot_flowgrid(load('FlowGrid.txt'))
