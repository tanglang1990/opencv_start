import cv2


rgb_cat = cv2.imread("images/cat.png")

gray_cat = cv2.cvtColor(rgb_cat, cv2.COLOR_BGR2GRAY)

cv2.imwrite("images/cat_gray.png", gray_cat)






