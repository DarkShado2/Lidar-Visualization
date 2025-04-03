import numpy as np
import open3d as o3d
import os
import glob
import time

def load_lidar_bin(file_path):
    #Loads lidar data from a .bin file
    scan = np.fromfile(file_path, dtype=np.float32)
    points = scan.reshape((-1, 4))  # x, y, z, reflectance
    return points

def create_grid_lines(z_level=-2, size=100, spacing=5, color=[0.7, 0.7, 0.7]):
    #Creates a grid of lines at a specified z-level
    lines = []
    points = []
    line_indices = []

    for i in range(-size, size + 1, spacing):
        # Horizontal lines
        points.append([i, -size, z_level])
        points.append([i, size, z_level])
        line_indices.append([len(points) - 2, len(points) - 1])

        # Vertical lines
        points.append([-size, i, z_level])
        points.append([size, i, z_level])
        line_indices.append([len(points) - 2, len(points) - 1])

    line_set = o3d.geometry.LineSet(
        o3d.utility.Vector3dVector(points),
        o3d.utility.Vector2iVector(line_indices)
    )

    line_set.paint_uniform_color(color)
    return line_set

def visualize_points(points):
    #Visualizes the point cloud with grid lines
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points[:, :3])  # Use only x, y, z coordinates

    # Create grid lines
    grid_lines = create_grid_lines()

    # Add both point cloud and grid lines to the visualization
    o3d.visualization.draw_geometries([pcd, grid_lines])


def process_lidar_video(lidar_folder):
    #Processes a folder of lidar .bin files and visualizes them sequentially
    file_list = sorted(glob.glob(os.path.join(lidar_folder, "*.bin")))

    for file_path in file_list:
        print(f"Processing: {file_path}")
        points = load_lidar_bin(file_path)
        visualize_points(points)
        time.sleep(0.1)  # Adjust delay for desired speed
        o3d.visualization.destroy_window()

#Folder Path
lidar_folder = r"Test_Data_short"
process_lidar_video(lidar_folder)