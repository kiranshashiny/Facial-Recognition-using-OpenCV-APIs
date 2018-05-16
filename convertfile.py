# Python script to convert a Jpeg to a Png
# To be completed.
# Remove the extension png in the final file name

import glob
from PIL import Image
import os

files=glob.glob('*.png')
for file in files:
	print (file)

	#file="leftroadsign.3.3.png"

	im = Image.open(file)
	im.convert('RGB').save(file+".jpeg","JPEG")
	newfile=file+".jpeg"
	print ( newfile )
	newfile=newfile.replace(".png","")
	print ("after replacing", newfile)
	os.rename (file,newfile )
