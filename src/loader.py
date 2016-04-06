from flowgrid import FlowGrid
import numpy as np
from re import findall

###################################################################################################################################################################################
## TOKENS
###################################################################################################################################################################################
TOKEN_DOCUMENTATION = '#'
TOKEN_RESOLUTION = 'RES'
TOKEN_MINIMUM = 'MIN'
TOKEN_MAXIMUM = 'MAX'

###################################################################################################################################################################################
## REGEX
###################################################################################################################################################################################
REGEX_FLOAT = r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
REGEX_UINT  = r"[0-9]+"

###################################################################################################################################################################################
## LOADER
###################################################################################################################################################################################
def load(fname):
    flowgrid = None

    with open(fname, 'r') as f:
        for line in f:
        
            if line.startswith(TOKEN_DOCUMENTATION):
                continue
            if line.startswith(TOKEN_RESOLUTION):
                flowgrid = FlowGrid(np.array(map(int, findall(REGEX_UINT, line))))
                print('Resolution: ' + str(flowgrid.voxels.shape))
                continue
            if line.startswith(TOKEN_MINIMUM):
                flowgrid.pMin = np.array(map(float, findall(REGEX_FLOAT, line)))
                print('Minimum: ' + str(flowgrid.pMin))
                continue
            if line.startswith(TOKEN_MAXIMUM): 
                flowgrid.pMax = np.array(map(float, findall(REGEX_FLOAT, line)))
                print('Maximum: ' + str(flowgrid.pMax))
                continue
                
            if not flowgrid:
                print('Error: ' + line)
                break
           
            e = map(np.uint64, findall(REGEX_UINT, line))
            flowgrid[tuple(e[:3])].set_access_counts(np.array(e[3:]))
    
    return flowgrid