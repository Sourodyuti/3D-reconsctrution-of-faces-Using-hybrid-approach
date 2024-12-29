# Step 5: Visualization (Classical + ML)
# File: scripts/visualize.py
import open3d as o3d

def visualize_point_cloud(points):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    o3d.visualization.draw_geometries([pcd])

if __name__ == "__main__":
    from dense_reconstruction import densify_sparse_points
    from reconstruction import reconstruct_sparse

    sparse_points, _, _ = reconstruct_sparse([], [], [])
    dense_points = densify_sparse_points(sparse_points)

    visualize_point_cloud(dense_points)
    print("Point cloud visualized.")
