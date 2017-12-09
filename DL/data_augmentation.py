# created: Julius, 09.12.2017

# all the functions to augment the dataset artificially
# functions added here should take one image as numpy array and additional parameters and return one modified image of the same size

# imports: 
import numpy as np

# shift the pixels of the image by a specified amount, an fill with zeros
def shift(image, x_shift, y_shift):
	# TODO: add functionality
	return shifted_image

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

