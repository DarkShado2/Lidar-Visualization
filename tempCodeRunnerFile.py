for file_path in file_list:
        print(f"Processing: {file_path}")
        points = load_lidar_bin(file_path)
        filtered_points = remove_noise(points)
        no_ground_points = remove_ground_points(filtered_points)
        final_points, bounding_boxes, final_labels = cluster_and_bounding_boxes(no_ground_points)  # Get filtered points
        if final_points.size > 0:
            visualize_bounding_boxes(final_points, bounding_boxes, final_labels)

            # Save the processed points to a new .bin file
            output_file_name = os.path.basename(file_path)
            output_file_path = os.path.join(output_folder, output_file_name)
            save_lidar_bin(final_points, output_file_path)
            print(f"Saved processed data to: {output_file_path}")

        time.sleep(0.1)  # Adjust delay for desired speed
        o3d.visualization.destroy_window()