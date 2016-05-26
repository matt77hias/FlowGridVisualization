# FlowGridVisualization
Visualization utilities for FlowGrids

~~~~{.python}
# Import a FlowGrid from a .txt file
from loader import load
flowgrid = load('FlowGrid.txt')

# Use one out of three methods for visualizing the FlowGrid 
from visualizer import plot_flowgrid_dots, plot_flowgrid_stack, plot_flowgrid
plot_flowgrid_dots(flowgrid)
plot_flowgrid_stack(flowgrid)
plot_flowgrid(flowgrid)
~~~~
