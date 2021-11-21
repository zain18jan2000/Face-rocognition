# Face-rocognition
Implementation of Face recognizer with OpenCV in Python<br/>

<h3>What is a Face recognizer ?</h3>
<p> A face Recognizer is a program or software used for identifying or verifying the identity of an individual by using their face. It is different from a face detection program because a face detector detects the face of a individual wheras a face recognizer can differentiate between two different faces. </p>

<h3>Implementation of face recognition program </h3>
<h4>Dataset:</h4>
<p>Dataset is the images of the individuals we want to differentiate on the basis of their faces. Create a folder for dataset and create sub-folders in it and to each sub-folder give the name of an individual.These names will be the labels in our program. Now each sub-folder represents a person. add the images of individuals in their corresponding folders. Every folders must have atleast 25-30 images for training. </p>

<h4>Feature Extraction:</h4>
<p> After arranging the dataset as mentioned above, we need to extract features from images and their labels as well. For that we will use  <b>feature extractor.py</b> . This program will provide us 3 files. </p>
1- <b>labels.npy</b> </br>
2- <b>images.npy</b> </br>
3- <b>encoded_labels.npy</b> </br>
</br>
<p><b>labels.npy</b> contains all the labels, <b>images.npy</b> contains the extracted features of images and <b>encoded_labels.npy</b> also contains labels but in encoded form.  </p>

<h4>Training:</h4>
<p>After preparing the dataset for training we will train a built in model of OpenCV for face recognition. For that we will use <b>train_reconizer.py</b>. This python program requires those 3 files which were created in the previous step. Make sure that those 3 files and <b>train_reconizer.py</b> are in the same folder. When we will execute <b>train_reconizer.py</b>, it will provide us file named as <b>face_recognize.yml</b> which is a trained model<p>  

<h4>Recognizing faces:</h4>
<p>After training the face recognition model we can now use it to recognize faces. We have 2 program to use this trained model. <b>face_recognize_pic.py</b> which is basically a simple web based application implemented using the <b>flask<b> module to recognize faces from images and <b>face_recognize_vid.py</b> which is for recognizing faces in videos. Make sure that these programes and <b>face_recognize.yml</b> are in the same folder.</p>

<h4>Limitations:</h4>
<p>
The face recognizing program we have implemented can be used only for single person images. <br>
The model accuracy will increase if trained with large number of images but this method of training the model can not be used for very large datasets.
</p>
