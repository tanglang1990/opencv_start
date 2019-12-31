import cv2

# 使用opencv读取刚刚写入的图片，查看像素内容，查看形状或者说维度信息

# 1.通过opencv库读取图片
src = cv2.imread("images/demo3x2.png")
# 2. 查看像素内容
print(src)
# 3. 查看维度信息
print(src.shape) # (3, 2, 3)


