# Step 1: Image Preprocessing (Classical)
# File: scripts/preprocess.py
import cv2
import os

def load_images(image_folder):
    images = []
    for fname in os.listdir(image_folder):
        if fname.endswith(('.jpg', '.png')):
            img = cv2.imread(os.path.join(image_folder, fname))
            if img is not None:
                images.append(img)
    return images

def preprocess_image(image):
    # Resize and convert to grayscale
    resized = cv2.resize(image, (512, 512))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    return gray

if __name__ == "__main__":
    image_folder = "../data/images"
    images = load_images(image_folder)
    processed_images = [preprocess_image(img) for img in images]
    print("Images preprocessed.")