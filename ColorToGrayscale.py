import cv2

img_name = input("Please enter a picture name in this folder: ")
img = cv2.imread(img_name)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("output.jpg", img_gray)
cv2.imshow("Original Image", img)
cv2.imshow("New Image", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()