import sys
import cv2
import numpy

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')

classifier = 'lbpcascade_frontalface.xml'
classifier_path='/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/'

faceCascade= cv2.CascadeClassifier(classifier_path+classifier)

print ( len( sys.argv ))

if ( len ( sys.argv) > 1) :
	image_name=sys.argv[1]
	print ("filename ", image_name)


	img = cv2.imread(image_name)
	font = cv2.FONT_HERSHEY_SIMPLEX
	print ("Am I here" )
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces=faceCascade.detectMultiScale(gray, 1.2,5)
else :
	print (" Please provide the name of the image file to process as an argument")
	quit()
	
