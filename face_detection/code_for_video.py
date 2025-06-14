import cv2

alg = "haarcascade_frontalface_default.xml" #selecting algorithm

haar_cascade = cv2.CascadeClassifier(alg) #loading algorithm


video = "video.mp4"
#img = cv2.imread(image)

cam = cv2.VideoCapture(video) #video id initialization

while True:
    ret,img = cam.read() #reading the frame from camera

    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting color image to gray

    faces = haar_cascade.detectMultiScale(grayImg,1.3,4) #getting coordinates

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,55,255), 6)
    cv2.imshow("FaceDetection", img)

    key = cv2.waitKey(10)
    print(key)
    if key == ord("s"):
        break

#cam.release()
##cv2.destroyAllWindows()
    
    
