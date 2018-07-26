import numpy as np

def conv2d(image, kernel):
	
	# Flip the kernel in both hor and vert directions
	kernel = np.flipud(np.fliplr(kernel))
	output = np.zeros_like(image)
	
	# padding
	image_padded = np.zeros_like((image.shape[0] + 2 , image.shape[1] + 2))
	
	image_padded[1:-1,1:-1] = image
	
	#traverse
	for x in range(image_padded.shape[1]):
		for y in range(image_padded.shape[0]):
			output[y,x] = (kernel * image_padded[y:y+3,x:x+3]).sum()
			
			
	return output
	
image = np.random.rand(5,5)
kernel = np.ones((3,3))

print(conv2d(image, kernel))
	
