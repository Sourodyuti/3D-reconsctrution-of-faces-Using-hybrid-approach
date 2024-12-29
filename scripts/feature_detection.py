# Step 2: Feature Detection (Classical)
# File: scripts/feature_detection.py
import cv2

def detect_features(image):
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(image, None)
    return keypoints, descriptors

def match_features(descriptors1, descriptors2):
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches

if __name__ == "__main__":
    from preprocess import load_images, preprocess_image

    image_folder = "../data/images"
    images = load_images(image_folder)
    processed_images = [preprocess_image(img) for img in images]

    kp1, des1 = detect_features(processed_images[0])
    kp2, des2 = detect_features(processed_images[1])
    matches = match_features(des1, des2)

    print(f"Detected {len(matches)} matches between the first two images.")
