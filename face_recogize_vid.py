import cv2
import numpy as np

cap = cv2.VideoCapture(r'D:\my files\arduino\respberry pi setup\Lesson # 1 (Normal Setup of Pi).mp4')

# # using CascadeClassifier to detect face
classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

labels = np.load("labels.npy",allow_pickle = True)
labels = labels.tolist()

face_recog = cv2.face.LBPHFaceRecognizer_create()
# read the trained model
face_recog.read('face_recognize.yml')

if (cap.isOpened()== False):
    print("Error opening video stream or file")

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    image = cv2.resize(frame,(750,500))

    if ret == True:
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        boxes = classifier.detectMultiScale(gray,minNeighbors = 9)
        for box in boxes:
            global x,y,width,height
            x,y,width,height = box
            global face
            face = gray[y:y+height,x:x+width]
            break
        cv2.rectangle(image,(x,y),(x+width, y+height),(0,255,0),thickness = 5)
       
        # prediction    
        label,confidence = face_recog.predict(face)
       
        # put the predicted label on frame 
        cv2.putText(image,labels[label],(x,y-1),
         cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2) 
        # Display the resulting frame
        cv2.imshow('Frame', image)
       
        if cv2.waitKey(10) == ord('q'):
            break
    else:
        print('Unable to read frame') 
        break   

# When everything done, release 
# the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()    