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

def draw_aumgented(bbox,ids,image,imgAug):

	if(len(ids) < 4):
		return []

	for id in range(len(ids)):
		if(ids[id] == 100):
			lt = (int(bbox[id][0][0][0]),int(bbox[id][0][0][1]))
		if(ids[id] == 101):
			rt = (int(bbox[id][0][1][0]),int(bbox[id][0][1][1]))
		if(ids[id] == 102):
			lb = (int(bbox[id][0][2][0]),int(bbox[id][0][2][1]))
		if(ids[id] == 103):
			rb = (int(bbox[id][0][3][0]),int(bbox[id][0][3][1]))
	
	h, w, c = imgAug.shape

	pts1 = np.array([lt,rt,lb,rb])
	pts2 = np.float32([[0,0],[w,0],[w,h],[0,h]])
	matrix, _ = cv.findHomography(pts2,pts1)
	imgout = cv.warpPerspective(imgAug,matrix,(image.shape[1],image.shape[0]))

	cv.fillConvexPoly(image,pts1.astype(int),(0,0,0))
	imgout = image + imgout
	
	cv.line(image,lt,rt,(0,0,255),3)
	cv.line(image,rt,lb,(0,255,0),3)
	cv.line(image,lb,rb,(255,0,0),3)
	cv.line(image,rb,lt,(255,255,255),3)

	return imgout

cap = cv.VideoCapture(0)
image_path = 'Vision/rick_asley/'
filename = 'giphy-'
dictionary = cv.aruco.Dictionary_get(cv.aruco.DICT_4X4_250)
parameters =  cv.aruco.DetectorParameters_create()
frame = 0

while 1:
	ret, img = cap.read()
	#test = np.zeros((300,400))
	gif_frame = frame % 32

	imgAug = cv.imread(str(image_path + filename + str(gif_frame+1) + '.jpg'),cv.IMREAD_COLOR)

	found_markers = find_aruco(img)

	if(len(found_markers[0]) != 0):
		test1 = draw_aumgented(found_markers[0],found_markers[1],img,imgAug)
		if(len(test1) != 0):
			img = test1
		else:
			frame = 0
	

	cv.imshow('img',img)
	#cv.imshow('rest',test)
	k = cv.waitKey(30) & 0xff
	if (k == 27):
		break
	
	frame += 1
	
# Close the window
cap.release()

# De-allocate any associated memory usage
cv.destroyAllWindows()
