#!/usr/bin/python3

#================================================================================================
#
#  FILE:
#	png.sh
#
#  DESCRIPTION:
# 	Visualize image file. 
#
#  USAGE:
#	chmod u+x png.sh
#	./png.sh
#
#
#================================================================================================


import sys
import matplotlib.pyplot as plt
import matplotlib.image as img 


img=img.imread(sys.argv[1])
plt.imshow(img)
plt.show()

# Alternative implementation

#from PIL import Image
#image=Image.open(sys.argv[1])
#image.show()
#plt.show()


