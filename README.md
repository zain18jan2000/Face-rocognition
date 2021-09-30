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
<p><b>labels.npy</b> contains all the labels, <b>images.npy</b> contains the extracted features of images and <b>encoded_labels.npy</b> also contains labels but in encoded form.  </p><br>
<br>
<h4>Training:</h4>
<p>After preparing the dataset for training we will train a builtin model of OpenCV for face recognition. For traing we will use <p>  
