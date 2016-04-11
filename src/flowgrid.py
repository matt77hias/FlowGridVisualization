import numpy as np

###################################################################################################################################################################################
## FlowGridVoxel
###################################################################################################################################################################################
class FlowGridVoxel(object):
    
    def __init__(self):
        self.set_access_counts()
    
    def set_access_counts(self, access_counts=np.zeros((7), dtype=np.uint64)):
        self.access_counts = access_counts
        
    def __getitem__(self, index):
        return self.access_counts[index] 

    def get_total_access_counts(self):
        return np.sum(self.access_counts)
   
###################################################################################################################################################################################
## FlowGrid
###################################################################################################################################################################################     
class FlowGrid(object):
    
    def __init__(self, resolution, pMin=np.ones((3)), pMax=np.ones((3))):
        # AABB data
        self.pMin = pMin
        self.pMax = pMax
        # Grid Voxels
        self.voxels = np.empty(resolution, dtype=FlowGridVoxel)
        flatten = self.voxels.flat
        for index in range(len(flatten)):
            flatten[index] = FlowGridVoxel()
        
    def __getitem__(self, index):
        return self.voxels[index]