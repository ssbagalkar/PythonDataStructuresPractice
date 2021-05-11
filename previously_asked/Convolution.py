import numpy as np

def conv2d(image, kernel, mode):
	
	# Flip the kernel in both hor and vert directions
	kernel = np.flipud(np.fliplr(kernel))

	
	# padding
	if mode == 'same':
		output = np.zeros_like(image)
		p_x = kernel.shape[0]//2
		p_y = kernel.shape[0]//2
		image_padded = np.zeros((image.shape[0] + 2 * p_x, image.shape[1] + 2 * p_y))

		image_padded[p_x:-p_x, p_y:-p_y] = image
	else:
		output = np.zeros(((image.shape[0]-kernel.shape[0])+1, (image.shape[1]-kernel.shape[1])+1))
		image_padded = image
	
	#traverse
	if mode == 'same':
		for x in range(image.shape[0]):
			for y in range(image.shape[1]):
				output[y, x] = (kernel * image_padded[y:y+kernel.shape[0], x:x+kernel.shape[0]]).sum()

	else:
		# traverse
		for x in range(output.shape[0]):
			for y in range(output.shape[1]):
				output[y, x] = (kernel * image_padded[y:y + kernel.shape[0], x:x + kernel.shape[0]]).sum()

	return output
	
image = np.random.rand(5,5)
kernel = np.ones((3,3))

print(conv2d(image, kernel, 'valid'))