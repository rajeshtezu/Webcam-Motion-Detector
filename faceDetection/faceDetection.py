import cv2
import glob

# create face CascadeClassifier object which will be used for face detction
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


images = glob.glob("*.jpg")
print(images)

for image in images:
    # read image
    img = cv2.imread(image)  # original form
    img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting into gray scale for better detction

    # start detection
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5)

    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)

    print(type(faces))
    print(faces)


    # showing the image
    cv2.imshow("Rajesh", img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
