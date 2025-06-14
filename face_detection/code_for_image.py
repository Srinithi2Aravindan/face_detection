import cv2

alg = "haarcascade_frontalface_default.xml" #selecting algorithm

haar_cascade = cv2.CascadeClassifier(alg) #loading algorithm


image = "image.jpg"
img = cv2.imread(image)

##cam = cv2.VideoCapture(0) #camera id initialization

while True:
##    _,img = cam.read() #reading the frame from camera

    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting color image to gray

    face = haar_cascade.detectMultiScale(grayImg,1.3,4) #getting coordinates

    for(x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
    cv2.imshow("FaceDetection", img)

    key = cv2.waitKey(10)
    print(key)
    if key == ord("s"):
        break

#cam.release()
cv2.destroyAllWindows()
    
    
