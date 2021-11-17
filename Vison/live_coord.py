import cv2 as cv
import numpy as np

def find_aruco(image,search_id = None,dict= cv.aruco.DICT_4X4_250):
	dictionary = cv.aruco.Dictionary_get(dict)
	parameters =  cv.aruco.DetectorParameters_create()
	markercorners, id, failed = cv.aruco.detectMarkers(image, dictionary, parameters=parameters)

	if(search_id != None and len(markercorners) != 0):
		
		for marker in range(len(id)):
			if(id[marker] == search_id):
				return [[markercorners[marker]],[id[marker]]]
	
	if(search_id == None):

		return [markercorners,id]

	return [(),None]

def draw_aruco_marker(image,markercorners,ids):

	for marker in range(len(ids)):
		
		corner = []
		for i in range(4):
			corner.append((int(markercorners[marker][0][i][0]),int(markercorners[marker][0][i][1])))

		cv.line(image,corner[0],corner[1],(0,0,255),3)
		cv.line(image,corner[1],corner[2],(0,255,0),3)
		cv.line(image,corner[2],corner[3],(255,0,0),3)
		cv.line(image,corner[3],corner[0],(255,255,255),3)

def draw_aumgented(bbox,ids,image):

	imgout = np.zeros((210,870),dtype = "uint8")


	if(len(ids) < 4):
		return imgout

	for id in range(len(ids)):
		if(ids[id] == 100):
			lt = (int(bbox[id][0][3][0]),int(bbox[id][0][3][1]))
		if(ids[id] == 101):
			rt = (int(bbox[id][0][2][0]),int(bbox[id][0][2][1]))
		if(ids[id] == 102):
			lb = (int(bbox[id][0][1][0]),int(bbox[id][0][1][1]))
		if(ids[id] == 103):
			rb = (int(bbox[id][0][0][0]),int(bbox[id][0][0][1]))
	
	h, w = imgout.shape
	pts1 = np.array([lt,rt,lb,rb])
	pts2 = np.float32([[0,0],[w,0],[w,h],[0,h]])
	matrix, _ = cv.findHomography(pts1,pts2)
	imgout = cv.warpPerspective(image,matrix,(imgout.shape[1],imgout.shape[0]))
#
	cv.line(image,lt,rt,(0,0,255),1)
	cv.line(image,rt,lb,(0,255,0),1)
	cv.line(image,lb,rb,(255,0,0),1)
	cv.line(image,rb,lt,(255,255,255),1)

	return imgout


def create_contour_image(image, thres_min = 120, thres_max = 255):
	gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
	blur = cv.GaussianBlur(gray,(1,1),1000)
	flag, thres = cv.threshold(blur,thres_min,thres_max,cv.THRESH_BINARY)
	return thres


cap = cv.VideoCapture(1)

cap.set(cv.CAP_PROP_FRAME_WIDTH, 1270)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
dictionary = cv.aruco.Dictionary_get(cv.aruco.DICT_4X4_250)
parameters =  cv.aruco.DetectorParameters_create()
frame = 0

while 1:
	ret, img = cap.read()
	
	found_markers = find_aruco(img)
	imgout = np.zeros((210,870),dtype = "uint8")
	img_gray = imgout
	if(len(found_markers[0]) >= 4):
		imgout = draw_aumgented(found_markers[0],found_markers[1],img)
		img_thres = create_contour_image(imgout)
		cv.imshow('out',imgout)
		cv.imshow('gray',img_thres)

	
	

	cv.imshow('img',img)
	

	k = cv.waitKey(30) & 0xff
	if (k == 27):
		break


	
# Close the window
cap.release()

# De-allocate any associated memory usage
cv.destroyAllWindows()
