import cv2

# imread is used to read an image by passing the path of image as input
img = cv2.imread("sub.png", cv2.IMREAD_COLOR)
# There are 3 parameters to read an image - 
#cv2.IMREAD_COLOR (1) => Specify to load the image in color
#cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged

# imshow is used to show the loaded image in a new window with a title
cv2.imshow("Pikachu Image", img)

# To hold the window until the user presses a key on keyboard
cv2.waitKey(0)

# delete / close the image window after the key pressed
cv2.destroyAllWindows()


##### Read and display an image in grayscale 

import cv2

img = cv2.imread("sub.png", 0)
cv2.imshow("Pikachu in Grayscale", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##### save an image using openCV after some change

import cv2
# OS library to handle the directory functionalities
import os

# change the path to where you wish to save the image
saved_directory = "C:/Downloads/Jetlearn/temp"


img = cv2.imread("sub.png", 0)
cv2.imshow("Pikachu in Black and White", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Change the current execution directory to 
os.chdir(saved_directory)

# write image to this directory
cv2.imwrite("pikaBlackWhite.png", img)
print("Successfully Saved")

##### Print an image in different color formats
# OpenCV default color format is RGB

import cv2
  
image = cv2.imread("pika.png", 1)
# Split the above image in red, blue and green different saturations
B, G, R = cv2.split(image)
  
cv2.imshow("original", image)
cv2.waitKey(0)
  
cv2.imshow("Blue Saturation Image", B)
cv2.waitKey(0)
  
cv2.imshow("Green Saturation Image", G)
cv2.waitKey(0)
  
cv2.imshow("Red Saturation Image", R)
cv2.waitKey(0)
  
cv2.destroyAllWindows()
