import pcl
import numpy as np
import pcl.pcl_visualization

# from pcl.pcl_registration import icp, gicp, icp_nl

cloud = pcl.load_XYZRGB('./examples/pcldata/tutorials/table_scene_mug_stereo_textured.pcd')
visual = pcl.pcl_visualization.CloudViewing()

# PointXYZ
# visual.ShowMonochromeCloud(cloud)

# visual.ShowGrayCloud(cloud, b'cloud')
visual.ShowColorCloud(cloud, b'cloud')
# visual.ShowColorACloud(cloud, b'cloud')

# while True:
#     visual.WasStopped()
# end

flag = True
while flag:
    flag != visual.WasStopped()
end

def point_cloud(self, depth):
    rows, cols = depth.shape
    c, r = np.meshgrid(np.arange(cols), np.arange(rows), sparse=True) #meshgrid the 2d array to put a 3rd dimension into it
    valid = (depth > 0) & (depth < 255)
    z = np.where(valid, depth / 256.0, np.nan) #Pixels with invalid depth in the input have NaN for the z-coordinate in the result.
    x = np.where(valid, z * (c - self.cx) / self.fx, 0)
    y = np.where(valid, z * (r - self.cy) / self.fy, 0)
    return np.dstack((x, y, z)) #restack columns
pass
