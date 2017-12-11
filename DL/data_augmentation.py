# created: Julius, 09.12.2017

# all the functions to augment the dataset artificially
# functions added here should take one image as numpy array and additional parameters and return one modified image of the same size

# imports: 
import numpy as np

# shift the pixels of the image by a specified amount, and fill with zeros; positive and negative parameters possible
# WORKS FOR GREYSCALE ONLY (only one color channel expected)
def shift(image, y_shift, x_shift):
	# get image shape and magnitude of shifts:
	w,h,d = image.shape
	d_x = abs(x_shift)
	d_y = abs(y_shift)
	# create new image with increased shape (increased by twice the shift magnitudes):
	shifted_image = np.zeros((w+2*d_x,h+2*d_y,d))
	# copy values of the original image to the center of the new image:
	shifted_image[d_x:w+d_x, d_y:h+d_y,:] = image
	# cut and return the new image according to the positive/negative shift parameters:
	return shifted_image[d_x-x_shift:w+d_x-x_shift, d_y-y_shift:h+d_y-y_shift, :]

# rotate the pixels by a specified angle, rotational center = image center
def rotate(image, angle):
	# TODO: add functionality
	return rotated_image

# zoom into specified region of the image (includes stretching if ratio of edge lengths is changed)
def zoom(image, x1, y1, x2, y2):
	# TODO: add functionality
	return zoomed_image

# blur the image, with amount of blurring specified by sigma
def gaussian(image, sigma):
	# TODO: add functionality
	return blurred_image

# add noise of specified intensity to the image 
def noise(image, intensity):
	# TODO: add functionality
	return noised_image

# TODO: add more functions

a = np.ones((3,4))
a = a.reshape((3,4,1))
print(a)
print("---")
b = shift(a,2,0)
print(b.reshape(3,4))


