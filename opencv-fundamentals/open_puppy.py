import cv2

img = cv2.imread("../Computer-Vision-with-Python/DATA/00-puppy.jpg")
while True:
    cv2.imshow("puppy", img)
    if cv2.waitKey(1) & 0xFF == 27: #27 is the ESC key
        break

cv2.destroyAllWindows()
