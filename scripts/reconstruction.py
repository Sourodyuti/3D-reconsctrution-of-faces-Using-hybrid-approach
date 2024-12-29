# Step 3: Sparse Reconstruction (Classical)
# File: scripts/reconstruction.py
import cv2
import numpy as np
import open3d as o3d

def reconstruct_sparse(matches, keypoints1, keypoints2):
    # Convert keypoints to points
    points1 = np.float32([kp.pt for kp in keypoints1])
    points2 = np.float32([kp.pt for kp in keypoints2])

    # Estimate Essential matrix
    E, _ = cv2.findEssentialMat(points1, points2, method=cv2.RANSAC, prob=0.999, threshold=1.0)

    # Recover camera pose
    _, R, t, _ = cv2.recoverPose(E, points1, points2)

    # Placeholder for 3D reconstruction
    sparse_points = np.random.rand(100, 3)  # Dummy data; replace with actual triangulation logic
    return sparse_points, R, t

if __name__ == "__main__":
    from feature_detection import detect_features, match_features
    from preprocess import load_images, preprocess_image

    image_folder = "../data/images"
    images = load_images(image_folder)
    processed_images = [preprocess_image(img) for img in images]

    kp1, des1 = detect_features(processed_images[0])
    kp2, des2 = detect_features(processed_images[1])
    matches = match_features(des1, des2)

    sparse_points, R, t = reconstruct_sparse(matches, kp1, kp2)
    print(f"Reconstructed sparse points: {sparse_points.shape}")