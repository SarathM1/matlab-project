from PIL import Image 
image_file = Image.open("MARS1.JPG") 	# open colour image
image_file = image_file.convert('1') 	# convert image to black and white directly
image_file.save('bw3.JPG')
image_file.show()
