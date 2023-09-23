import numpy as np
import cv2

blur_filter = np.array([
    [0.0187, 0.0563, 0.0563, 0.0187],
    [0.0562, 0.1187, 0.1187, 0.0562],
    [0.0562, 0.1187, 0.1187, 0.0562],
    [0.0187, 0.0563, 0.0563, 0.0187]
])

blurred_image = cv2.imread('blur_img.jpg', cv2.IMREAD_GRAYSCALE)

try:
    deblur_filter = np.linalg.inv(blur_filter)
except np.linalg.LinAlgError:
    print("The blur filter is not invertible.")
    deblur_filter = None

if deblur_filter is not None:
    deblurred_image = cv2.filter2D(blurred_image, -1, deblur_filter)
    cv2.imshow('Original Blurred Image', blurred_image)
    cv2.imshow('Deblur Img', deblurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()