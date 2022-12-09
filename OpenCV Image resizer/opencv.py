import cv2
import glob

# Passing image a color(1) or greyscale band(0) or transparency(-1)
img = cv2.imread("galaxy.jpg", 1)
print(type(img))
print(img)
print(img.shape)
print(img.ndim)

# # To resize the image
resized_image = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))

# To view the image on the window
cv2.imshow("Galaxy", resized_image)
# To save the resized image
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Batch Image Resizing
"""What glob does is that it creates a list 
all the files having .jpg as extension"""
images = glob.glob("*.jpg")
for image in images:
    img = cv2.imread(image, 0)
    resize = cv2.resize(img, (100, 100))
    cv2.imshow("Images", resize)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_" + image, resize)
