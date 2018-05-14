# Changes - I made recognizer.load -> recognizer-> read ()
# I added the full path to the xml file.
# The trainner.yml is in the current folder.
# Python3 detector.py
# 
import cv2
import numpy as np
import sys

# Feed in the name of the image to be processed as an argument.

if (len ( sys.argv) > 1) :
	image_name=sys.argv[1]
	print ("Image being processed : ", image_name)
else :
	print (" Please provide the name of the image file to process as an argument")
	quit()
	
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')

classifier = 'lbpcascade_frontalface.xml'
classifier_path='/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/'

faceCascade= cv2.CascadeClassifier(classifier_path+classifier)

img = cv2.imread(image_name)
font = cv2.FONT_HERSHEY_SIMPLEX

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(gray, 1.2,5)

if ( len (faces ) == 0) :
	print( "No identifiable faces found, Please select a correct image as input !")
	print( "Please check on the quality of the print, clarity of data in the image")
	print ("Try another image that is a little more clearer")
	quit()

for(x,y,w,h) in faces:
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        
        print ("Confidence level = " ,conf, " Id = ", Id )

        if ( conf > 50 ):
            print (" Cannot recognize this image, Check if the label[] has been assigned to this image in this code ");	
            print (" e.g:  dataSet folder to contain some training images")
            quit()
        elif (conf < 50):
            if ( Id == 9) :
                Id="DalaiLama"
                print ( "This is Dalai Lama's image")
                Id="Dalai"
                font                   = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,300)
                fontScale              = 1
                fontColor              = (255,255,255)
                lineType               = 2

                cv2.putText(img,'Dalai Lama ',
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)
                cv2.imshow('image',img)
                cv2.waitKey(0)

            elif (Id==1):
                print ( "This is Trump's image")
                Id="Trump"
                font                   = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,300)
                fontScale              = 1
                fontColor              = (255,255,255)
                lineType               = 2
        
                cv2.putText(img,'Trump ',
        		bottomLeftCornerOfText,
        		font,
        		fontScale,
        		fontColor,
        		lineType)
                cv2.imshow('image',img) 
                cv2.waitKey(0)

            else:
                print ( "This is NOT Trump's ")
                Id="Unknown"
                font                   = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,300)
                fontScale              = 1
                fontColor              = (255,255,255)
                lineType               = 2

                cv2.putText(img,'Unknown User !',
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)
                cv2.imshow('im',img) 
                cv2.waitKey(10)


cv2.destroyAllWindows()
