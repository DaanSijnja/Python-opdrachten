import cv2 as cv
import numpy as np
import math as mth




def draw_fig(img,fig,color=(255,255,255)):
    h, w, c = img.shape
    for line in fig:
        p1 = line[0][0:2]
        p2 = line [1][0:2]

        p1 = [int(p1[0])+(h//2),int(p1[1])+(w//2)]
        p2 = [int(p2[0])+(h//2),int(p2[1])+(w//2)]
        cv.line(img,p1,p2,color)

    return img

def matrix_point_vgm(p,m):
    new_point = [0,0,0]

    new_point[0] = p[0]*m[0][0] + p[1]*m[0][1] + p[2]*m[0][2]
    new_point[1] = p[0]*m[1][0] + p[1]*m[1][1] + p[2]*m[1][2]
    new_point[2] = p[0]*m[2][0] + p[1]*m[2][1] + p[2]*m[2][2]
    return new_point


def translate_fig(fig,trans_mat):
    new_fig = []
    for line in fig:
        p1_h = line[0][:]
        p2_h = line[1][:]

        p1 = matrix_point_vgm(p1_h,trans_mat)
        p2 = matrix_point_vgm(p2_h,trans_mat)


        new_fig.append([p1,p2])
        
    return new_fig


def perspective_fig(fig,plane,cam):
    d_plane_cam = cam[2] - plane[2]
    new_fig = []
    for line in fig:

        p1 = line[0][:]
        d_p1_cam = cam[2] - p1[2]

        p1[0] = p1[0]*abs(d_plane_cam/d_p1_cam)
        p1[1] = p1[1]*abs(d_plane_cam/d_p1_cam)

        p2 = line[1][:]
        d_p2_cam = cam[2] - p2[2]

        p2[0] = p2[0]*abs(d_plane_cam/d_p2_cam)
        p2[1] = p2[1]*abs(d_plane_cam/d_p2_cam)

        new_fig.append([p1,p2])

    return new_fig       


def create_rot_matrix(angle):
    a = angle[0]*mth.pi/180
    b = angle[1]*mth.pi/180
    c = angle[2]*mth.pi/180

    rot_mat = [
            [ mth.cos(a)*mth.cos(b), mth.cos(a)*mth.sin(b)*mth.sin(c) - mth.sin(a)*mth.cos(c), mth.cos(a)*mth.sin(b)*mth.cos(c) + mth.sin(a)*mth.sin(c)],
            [ mth.sin(a)*mth.cos(b), mth.sin(a)*mth.sin(b)*mth.sin(c) + mth.cos(a)*mth.cos(c), mth.sin(a)*mth.sin(b)*mth.cos(c) - mth.cos(a)*mth.sin(c)],
            [ -mth.sin(b), mth.cos(b)*mth.sin(c), mth.cos(b)*mth.cos(c)]
            ]

    return rot_mat




rot_mat = create_rot_matrix((1,2,3))

plane = [0,0,0]
camera = [0,0,-1000]

fig = [
        #voorkant
        [[-100,-100,100],[100,-100,100]],
        [[100,-100,100],[100,100,100]],
        [[100,100,100],[-100,100,100]],
        [[-100,100,100],[-100,-100,100]],
        #ribben voor naar achter
        [[-100,-100,100],[-100,-100,-100]],
        [[100,-100,100],[100,-100,-100]],
        [[100,100,100],[100,100,-100]],
        [[-100,100,100],[-100,100,-100]],
        #achterkant
        [[-100,-100,-100],[100,-100,-100]],
        [[100,-100,-100],[100,100,-100]],
        [[100,100,-100],[-100,100,-100]],
        [[-100,100,-100],[-100,-100,-100]],
        #midpoint
        [[0,0,0],[0,0,0]],
        

        ]

triagle = [
        #base
        [[-100,-100,-43.3],[-100,100,-43.3]],
        [[-100,100,-43,3],[100,100,-43.3]],
        [[100,100,-43.3],[100,-100,-43.3]],
        [[100,-100,-43.3],[-100,-100,-43.3]],
        #top
        [[-100,-100,-43.3],[0,0,43.3]],
        [[-100,100,-43,3],[0,0,43.3]],
        [[100,100,-43.3],[0,0,43.3]],
        [[100,-100,-43.3],[0,0,43.3]],
        #midpoint
        [[0,0,0],[0,0,0]],
        ]



fig_copy = triagle[:]

werkvlak = np.zeros((640,640,3),np.uint8)

while True:
    fig_copy = translate_fig(fig_copy,rot_mat)
 


    perspective = perspective_fig(fig_copy,plane,camera)
    
    new_werkvlak = draw_fig(werkvlak.copy(),perspective,(255,255,0))



    cv.imshow('werkvlak',new_werkvlak)

    k = cv.waitKey(30) & 0xff
    if (k == 27):
        break


cv.destroyAllWindows()







