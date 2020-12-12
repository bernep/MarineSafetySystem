import cv2
import time
import numpy as np

# For testing only:
# Read the input image
# img = cv2.imread('test.jpg')
############################
######    Sources:    ######
############################
# https://docs.opencv.org/master/da/d97/tutorial_threshold_inRange.html
# https://docs.opencv.org/3.4/d2/de8/group__core__array.html
# https://docs.python.org/3/library/time.html
# https://pyformat.info/
# https://docs.python.org/3/c-api/none.html
# https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html

##############################################################################################################
# Get webcam, read image from sensor:
# camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
##############################################################################################################
# Altertive, use video file: 
# camera = cv2.VideoCapture('aq2NQ-EHfGc_clip.mp4')
camera = cv2.VideoCapture('sample.mp4')
# Youtube Video: Key: aq2NQ-EHfGc
##############################################################################################################

# Initial values:
sleep_time = 0.01
consecutive_threshold = 10
fall = False
consecutive = 0
frame = 0

# Vary BGR by X% to allow color allocation:
# Yellows / Florescent:
MIN = np.array([0,140,140], np.uint8) #BGR order
MAX = np.array([90,255,255], np.uint8) #BGR order
# Red / Orange:
# MIN = np.array([0,220,60], np.uint8) #BGR order
# MAX = np.array([40,255,140], np.uint8) #BGR order

global colorFound #avg of pos color, cannot move much per frames
colorFound = [-1,-1,-1,-1]

##############################################################################################################
def trainCamera():
	#Funciton trains the camera to sense specific color, this takes an image and uses that to calibrate it
	time.sleep(10)
	camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
	return_value, image = camera.read()
	avg_for_row = np.average(image, axis=0)
	avg_tot = np.average(avg_for_row, axis=0)
	print(avg_tot)  #format: B,G,R
	MIN = np.array([max(avg_tot[0]-30,0),max(avg_tot[2]-30,0),max(avg_tot[1]-30,0)], np.uint8)
	MAX = np.array([min(avg_tot[0]+30,255),min(avg_tot[2]+30,255),min(avg_tot[1]+30,255)], np.uint8)
	print("Color read in from camera sensor")
	return MIN, MAX

# MIN, MAX = trainCamera()
##############################################################################################################
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def trackPerson(face_x,face_y):
	global colorFound
	minX=colorFound[0]-50
	minY=colorFound[1]-50
	maxX=colorFound[2]+50
	maxY=colorFound[3]+50
	if(face_x>minX and face_x<maxX and face_y>minY and face_y<maxY):
		return True
	return False

def findFace(image):
	global faceLock #change the global lastFace var
	# Convert into grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# Detect faces
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)
	target=False
	# Draw rectangle around the faces
	for (x, y, w, h) in faces:
		if(w>0):
			# found face that is not the target
			if(trackPerson((x+x+h)/2, (y+y+h)/2) == False):
				cv2.rectangle(image, (x, y), (x+w, y+h), (33, 255, 0), 3)
				cv2.putText(image, 'NOT TARGET', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (33, 255, 0), 2)
				continue
			#found a face, reset consecutive
			consecutive = 0
			#found face that is target:
			cv2.rectangle(image, (x, y), (x+w, y+h), (100, 100, 220), 3)
			cv2.putText(image, 'Rider detected', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 100, 220), 2)
			faceLock = [(x+x+h)/2, (y+y+h)/2]
			target=True
	cv2.putText(image, 'Faces detected: {}'.format(len(faces)), (90, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (40,250,250), 2)
	return len(faces), target

def findColor(image):
	global colorFound
	return_value, image2 = camera.read()
	data = np.asarray( image, dtype="int32" )
	dst = cv2.inRange( image, MIN, MAX )
	num_color = cv2.countNonZero(dst)
	coord = cv2.findNonZero(dst)

	if(coord is not None):
		#draw if color is found
		minX = coord[0][0][0]
		minY = coord[0][0][1]
		maxX = coord[len(coord)-1][0][0]
		maxY = coord[len(coord)-1][0][1]
		colorFound = [minX,minY,maxX,maxY]
		cv2.rectangle(image, (minX, minY), (maxX, maxY), (40, 225, 255), 2)
		cv2.putText(image, 'Color detected', (minX, maxY+20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (40,250,250), 2)

	cv2.putText(image, 'Color pixels: {}'.format(num_color), (90, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (40,250,250), 2)

	if(num_color>10): #Give buffer, use 10
		return num_color, True
	return num_color, False

##############################################################################################################

# Continuous camera loop:
start_time = time.time()
while True:
	frame=frame+1
	time.sleep(sleep_time)
	return_value, image = camera.read()
	color_ct, findColorReturn = findColor(image)
	# color_ct, findColorReturn = 0, True
	face_ct, findFaceReturn = findFace(image)
	# Display the output
	print('The number of yellow pixels is: ' + str(color_ct), '\tNumber of faces found: '+str(face_ct))
	if(consecutive >= consecutive_threshold):
		#reset vars:
		consecutive=0
		findColorReturn=False
		findFaceReturn=False
		#trigger flag:
		fall = True
		#off = True
		#prints:
		end_time = time.time()
		print("\n"+"#"*32)
		print("#"*7+" Detected fall!!! "+"#"*7)
		print("#"*32+"\n")
		print("Program analyzed {} frames".format(frame))
		print("Framerate: {:.3f} frame{} per second".format(frame/(end_time-start_time), "s" if int(frame/(end_time-start_time))!=1 else ""))
		print("Program completed and lasted {0:.3f} seconds.".format(end_time-start_time))
		print("\n\nSending signal to central control!\n")
		############################go to function to wait for button input to ressurrect function (instead of breaking)
		cv2.rectangle(image, (85, 300), (1200, 400), (50, 50, 50), 100)
		cv2.putText(image, 'FALL DETECTED', (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 5, (40,250,250), 9)
	cv2.imshow('img', image)
	cv2.waitKey(1)
	if(not findColorReturn and not findFaceReturn):
		consecutive += 1
	else:
		consecutive = 0

# End camema obj:
del(camera)
