# FlowGridVisualization

## About
A visualization tool for FlowGrids.

## Use
<p align="center"><img src="https://github.com/matt77hias/FlowGridVisualization/blob/master/res/Example.png" ></p>

~~~~python
# Import a FlowGrid from a .txt file
from loader import load
flowgrid = load('FlowGrid.txt')

# Use one out of three methods for visualizing the FlowGrid 
from visualizer import plot_flowgrid, plot_flowgrid_stack, plot_flowgrid_dots
plot_flowgrid(flowgrid)
plot_flowgrid_stack(flowgrid)
plot_flowgrid_dots(flowgrid)  #could not scale
~~~~
