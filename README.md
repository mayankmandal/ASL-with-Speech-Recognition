# ASL-with-Speech-Recognition
Hand Gesture depicting a sign of ASL from a live video

#WHAT IS ASL TRANSLATOR

It will take the input of hand gesture depicting a sign of ASL from a live video
It will then convert the image captured of sign to text and then to speech

FRONT END : For front end we have used PyQt5 library of python,
BACK END : For Back end ,We have created deep learning model of CNN in keras using Tensorflow backend and utilising numpy,os,pyttsx3 and openCV libraries


TECHNOLOGIES  – Computer Vision, Deep Learning.
TOOLS - Open CV, Ananconda
LANGUAGE - Python

#COMPLETE PROBLEM STATEMENT
1. Creating the dataset
2. Building and Compiling the CNN Model
3. Training the dataset on CNN model
4. Capturing and hence obtaining the video of the user signing (input) 
5. Loading the CNN model and predicting the output

PHASE 1 (CREATING DATASET)
Captured images from webcam
Taken around 400 images of each gesture in real time
Apply masking and setting hsv value to recognise only hand color
Splitting these images into train data and test data
80% of images are in train data and 20% in test data

PHASE 2(CNN MODEL)
Building the CNN Model
    -Adding Convolution Layer
    -Adding MaxPooling Layer
    -Adding Relu activation function
    -Flattening
    -Feeding to fully connected network
Compiling the CNN Model

PHASE 3(TRAINING DATASET)
Data Augmentation

Fitting model on Dataset
	-Setting the number of Epochs
	-Setting the number of step per epoch

PHASE 4(SIGN TO TEXT TO SPEECH)
A hand gesture of ASL will be taken as input from web cam
The gesture will be compared to trained dataset
The matched result of alphabet will be shown as text
The text is convered to Voice using a python library pyttsx3

DFD Steps
1.	Image sent for BGR to HSV Transformation	
2.	Outputs HSV Image			
3.	Image sent for Masking		
4.	Image is returned after masking		
5.	Sequence model is selected		
6.	Apply Convolution layer		
7.	Convolved image			
8.	Apply Pooling layer			
9.	Apply convolution			
10.	Convolved image			
11.	Apply pooling			
12.	Pooled matrix			
13.	Flattening
14.	Flattened image
15.	Add fully connected layer
16.	Fully connected network
17.	Compiling CNN
18.	Compiled Model
19.	Fitting CNN
20.	Trained Model
21.	Training
22.	Input generated from webcam
23.	Comparison with trained dataset
24.	Output
