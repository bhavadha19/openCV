import cv2
img = cv2.imread("pink aes.png",0)
print(img)
cv2.imshow('pink aes.png',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()