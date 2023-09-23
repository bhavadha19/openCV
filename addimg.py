import cv2

# Load the two images you want to add
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jfif')

# Ensure that both images have the same dimensions
# You can resize them if needed

# Add the two images
result = cv2.add(image1, image2)

# Display the result image
cv2.imshow('Added Image', result)
cv2.waitKey(0)  # Wait for a key press (0 means indefinitely)
cv2.destroyAllWindows()  # Close all OpenCV windows
