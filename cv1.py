import cv2
img = cv2.imread("pink aes.png",1)
print(img)
img2=img.copy()
cv2.imshow('pink aes.png',img)
cv2.waitKey(0)
cv2.imwrite("bava.png",img)
cv2.destroyAllWindows()