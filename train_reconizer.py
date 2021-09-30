from typing import no_type_check


import numpy as np
import cv2

# load the encoded labels
y_train = np. load("encoded_labels.npy")
# load the extracted features
x_train = np.load("images.npy", allow_pickle = True)

# train the recognizer
face_recog = cv2.face.LBPHFaceRecognizer_create()
face_recog.train(x_train,y_train)

# save the recognizer
face_recog.save('face_recognize.yml')

print('Training Done! MODEL saved as face_recognize.yml')