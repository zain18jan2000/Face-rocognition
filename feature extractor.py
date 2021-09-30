import cv2
import os
import numpy as np

classifier = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

path = input("Enter the path of dataset. Please use '/' instead of '\' when typing in directory path:") 
labels = os.listdir(path)
x_train = list()
y_train =  list()
for label in labels:
    Dir1 = os.path.join(path,label)
    files = os.listdir(Dir1)
    for file in files:
        Dir2 = os.path.join(Dir1,file)
        img = cv2.imread(Dir2)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        boxes = classifier.detectMultiScale(gray,minNeighbors = 9)
        for box in boxes:
            x,y,width,height = box
            x_train.append(gray[y:y+height,x:x+width])
            y_train.append(labels.index(label))
            break
x_train = np.array(x_train, dtype='object')
y_train =np.array(y_train)
labels = np.array(labels, dtype='object')
np. save("images.npy", x_train)
np.save("encoded_labels.npy", y_train)
np.save("labels",labels)

print("Features and other data extracted and saved for training in current directory")