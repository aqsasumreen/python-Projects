import cv2
video_cap = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"
faceCap = cv2.CascadeClassifier(cascPath)
# Runtime pr camer ko enable rny kaliy
# camer us time tk enable rhy jb tk koi key press na ho...
while True:
    ret, video_data = video_cap.read()
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces= faceCap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE)
    # ye sb face k feature ko coverup kia hy.
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("video_live", video_data)
    if cv2.waitKey(10) == ord('a'): # camera aik particular time kaliy enable rhy but jest hi key pree ho tou disable ho jaye
        break
video_cap.release()
# face ko detect krny kali5y
# cascPath = "haarcascade_frontalface_default.xml"
# eyePath = "haarcascade/haarcascade_eye.xml"
# smilePath = "haarcascade/haarcascade_smile.xml" faceCascade = cv2.CascadeClassifier(cascPath)
#eyeCascade = cv2.CascadeClassifier(eyePath)
# faceCap = cv2.CascadeClassifier(cascPath)
