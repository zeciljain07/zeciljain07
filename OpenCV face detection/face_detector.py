import cv2

# Face Detector
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("news.jpg")

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""Here scaleFactor having lower value
will get a higher accuracy will detecting the 
faces in images having big areas to scan"""
"""What python will basically do is, it will increase the 
area by 5% and search in a smaller area"""
"""What minNeighbours does is that it tells python
how many neighbours to search around the window"""
"""We can tweak with these two values and 
try to achieve the highest values"""
faces = face_cascade.detectMultiScale(gray_image,
                                      scaleFactor=1.1,
                                      minNeighbors=5)

print(type(faces))
print(faces)

# To access the faces array
for x, y, w, h in faces:
    img = cv2.rectangle(img,
                        (x, y),
                        (x + w, y + h),
                        (0, 255, 0),
                        3)

resized = cv2.resize(img, (int(img.shape[1] / 3), int(img.shape[0] / 3)))

cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
