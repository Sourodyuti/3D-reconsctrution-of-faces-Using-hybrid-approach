import cv2

# Load and resize an image
image = cv2.imread("image_path.jpg")
resized = cv2.resize(image, (512, 512))

# Show the image
cv2.imshow("Resized Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
