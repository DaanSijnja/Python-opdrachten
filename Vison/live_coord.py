import cv2 as cv
import numpy as np

blokjes = {
	"wit" : [(19,13,227),(38,47,255)],
	"blauw" : [(79,47,0),(115,255,88)],
	"geel" : [(9,108,190),(50,255,255)],
	"paars": [(147,0,32),(168,154,98)],
	"oranje":[(1,104,185),(15,255,255)]
}


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

	imgout = np.zeros((442,870),dtype = "uint8")


	if(len(ids) < 4):
		return imgout

	for id in range(len(ids)):
		if(ids[id] == 100):
			lt = (int(bbox[id][0][3][0]),int(bbox[id][0][3][1]))
		if(ids[id] == 101):
			rt = (int(bbox[id][0][2][0]),int(bbox[id][0][2][1]))
		if(ids[id] == 103):
			lb = (int(bbox[id][0][1][0]),int(bbox[id][0][1][1]))
		if(ids[id] == 102):
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


def create_contour_image(image, thres_min = 85, thres_max = 255):
	img_gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
	img_blur = cv.GaussianBlur(img_gray, (5, 5), 0)
	img_canny = cv.Canny(img_blur,thres_min,thres_max)
	kernel = np.ones((5, 5), np.uint8)
	img_dilate = cv.dilate(img_canny, kernel, iterations=1)

	return img_dilate

def find_contours(image):
	contours = cv.findContours(image,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
	contours = contours[0] if len(contours) == 2 else contours[1]
	return contours

def find_by_color(image,min_range,max_range,name):
	hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
	mask = cv.inRange(hsv, min_range, max_range)
	img_blur = cv.GaussianBlur(mask, (5, 5), 0)
	cnts = cv.findContours(img_blur,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if len(cnts) == 2 else cnts[1]

	for c in cnts:
		area = cv.contourArea(c)
		if(area > 1100):
			x, y, w, h  = cv.boundingRect(c)
			M = cv.moments(c)
			cx = int(M['m10']/M['m00']) # middepunt
			cy = int(M['m01']/M['m00'])	# middepunt
			cv.circle(image,(cx,cy),2,(255,0,0),5)
			#hull = cv.convexHull(c)
			#epsilon = 0.1*cv.arcLength(hull,True)
			#approx = cv.approxPolyDP(hull,epsilon,True)
			#cv.drawContours(image,approx,-1,(255,255,255),10)
			#cv.rectangle(image,(x, y), (x + w, y + h), (36,255,12), 2)
			cv.putText(image, name, (cx,cy-5), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
			cv.putText(image,'x: ' +  str(cx) + ' y: ' + str(cy) , (cx,cy+20), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))


	cv.imshow('screen', img_blur)


cap = cv.VideoCapture(0,cv.CAP_DSHOW)

cap.set(cv.CAP_PROP_FRAME_WIDTH, 1080)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 810)
dictionary = cv.aruco.Dictionary_get(cv.aruco.DICT_4X4_250)
parameters =  cv.aruco.DetectorParameters_create()


while 1:
	ret, img = cap.read()
	
	found_markers = find_aruco(img)

	draw_aruco_marker(img,found_markers[0],found_markers[1])

	imgout = np.zeros((210,870),dtype = "uint8")
	#img_cir = create_contour_image(img)
	img_gray = imgout
	if(len(found_markers[0]) >= 4):
		imgout = draw_aumgented(found_markers[0],found_markers[1],img)
		find_by_color(imgout,blokjes["blauw"][0],blokjes["blauw"][1],"Blauw")
		find_by_color(imgout,blokjes["geel"][0],blokjes["geel"][1],"Geel")
		find_by_color(imgout,blokjes["paars"][0],blokjes["paars"][1],"Paars")
		find_by_color(imgout,blokjes["oranje"][0],blokjes["oranje"][1],"Oranje")
		cv.imshow('out',imgout)
		

	
	

	cv.imshow('img',img)
	#cv.imshow('test',img_cir)

	k = cv.waitKey(30) & 0xff
	if (k == 27):
		break


	
# Close the window
cap.release()

# De-allocate any associated memory usage
cv.destroyAllWindows()
