# Face-rocognition
Implementation of Face recognizer with OpenCV in Python<br/>

<h3>What is a Face recognizer ?</h3>
<p> A face Recognizer is a program or software used for identifying or verifying the identity of an individual by using their face. It is different from a face detection program because a face detector detects the face of a individual wheras a face recognizer can differentiate between two different faces. </p>

<h3>Implementation of face recognition program </h3>
<h4>Dataset:</h4>
<p>Dataset is the images of the individuals we want to differentiate on the basis of their faces. Create a folder for dataset and create sub-folders in it and to each sub-folder give the name of an individual.These names will be the labels in our program. Now each sub-folder represents a person. Store the images of individuals in their coressponding folders. Every folders must have atleast 25-30 images for training. </p>

<h4>Feature Extraction:</h4>
<p> After preparing and arranging dataset as mentioned above, we need to extract features from images and their labels as well. For that we will use  <b>feature extractor.py</b> . This program will provide us 3 files. </p>
1- <b>labels.npy</b> </br>
2- <b>images.npy</b> </br>
3- <b>encoded_labels.npy</b> </br>
<p>labels.npy contains all the labels, images.npy contains the extracted features of images and encoded_labels.npy also contains labels but in encoded form.  </p>
