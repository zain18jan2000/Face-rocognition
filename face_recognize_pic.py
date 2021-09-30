from flask import Flask, render_template, request
import cv2
import numpy as np

labels = np.load("labels.npy",allow_pickle = True)
labels = labels.tolist()

app = Flask(__name__)

# set it to  true otherwise the new file chosen will not
# be displayed on  http://127.0.0.1:5000/after/
# basically refreshing the image on every selection and submission 
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = True

# using CascadeClassifier to detect face
classifier = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

face_recog = cv2.face.LBPHFaceRecognizer_create()
# read the trained model
face_recog.read('face_recognize.yml')


@app.route("/")
def index():
    return render_template('index.html')

# list of methods required when using  post method
# in index.html method is specified as post while performing an action on 
# the submission of form
@app.route("/after", methods = ['GET','POST'])
def after():
    
    # accessing file which have been submitted
    file = request.files["file1"]
    # saving  it to static folder as file.jpg
    file.save('static/file.jpg')
    # now load the saved image 
    image = cv2.imread('static/file.jpg')
    # resizing it
    img = cv2.resize(image, (400,400))
    # saving it again after resizing it
    cv2.imwrite('static/file.jpg',img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    boxes = classifier.detectMultiScale(gray,minNeighbors = 9)
    for box in boxes:
            x,y,width,height = box
            gray = gray[y:y+height,x:x+width]
            break
    # prediction    
    label,confidence = face_recog.predict(gray) 
    prediction = 'Person recognized as : '+  labels[label] 
    return render_template('predict.html', result = prediction)   

if __name__ == "__main__":
    app.run(debug=True)  