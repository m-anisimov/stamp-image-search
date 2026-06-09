import cv2

# завантаження зображення
image = cv2.imread("query/test_real_4.jpg")

# Gaussian Blur
blurred = cv2.GaussianBlur(image, (9, 9), 0)

# збереження
# cv2.imwrite("query/test_blur15.jpg", blurred)
cv2.imwrite("query/test_real_4_blur_9.jpg", blurred)


print("Blur image created!")