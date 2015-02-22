from PIL import Image

col = Image.open("MARS1.JPG")
gray = col.convert('L') 				# Converts image to grayscale
bw = gray.point(lambda x: 0 if x<128 else 255, '1')	# Uses lambda function to convert image to b&w (128=255/2)
bw.save("bw1_Result.JPG")
bw.show()


