# OpenCV_RecognizeFaces
This blog is about how to recognize, train and detect faces in still images.

The code can be modified to recognize faces in Video streams as well.

Here I have used the most commonly used algorigthm LBPH ( Local Binary Patterns Histogram) to recognize faces, train faces and predict faces.

The code is simple and is split into 2 parts.

1) Set up training so that this face gets recognized in future. The training involves reading the facial patterns and storing it in a flat file ( .yml file )
2) Predict and Recognize the new face that is provided.
User inputs the image file to be predicted and if this image exists in the trained data, then the image gets printed.


The dataset is stored in dataSet Folder in the current directory
The images (jpegs)belong to that of Trump and HH Dalai Lama.

You will notice that the file names/Ids on the Trump data set is '1' and HH Dalai Lama is set to '9', This distinguishes the labels for the face.


First, download and run the code as follows.

1. python3 trainer.py
 This will create the trainner.yml flat file containing the parameters of the images.

2. python3 detector_image.py
	This will detect the image in the trained library and if it can recognize then a rectangle is printed on the face, along with the name.

This can be further customized to user's specs. ( Just change the Id in the image.jpeg to whatever number you want.  e.g: Edison = 11, Think of this as a label to the image. )




Troubleshooting;
Check that the input file is present in the current folder when running the detector_image.py


Check that there are enough images in the /dataSet folder.

Additional references :

Histograms :

 
