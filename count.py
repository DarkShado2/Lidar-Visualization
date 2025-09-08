import numpy as np
import os

file_path = r"C:\Users\greer\Documents\GitHub\Lidar-Visualization\Processed_Data_short\0000000000.bin"

# Get file size in bytes
file_size = os.path.getsize(file_path)

# Each point is 4 floats (x, y, z, reflectance), each float = 4 bytes
point_size = 4 * 4  # 4 floats * 4 bytes each = 16 bytes per point

# Number of points
num_points = file_size // point_size
print(f"Number of points: {num_points}")
