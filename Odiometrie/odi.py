import cv2 as cv
import numpy as np
import math as mth
import PySimpleGUI as sg

height = 640
width = 640
gridsize = 16

class Line:
    def __init__(self,p1,p2,color):
        self.p1 = p1[:]
        self.p2 = p2[:]
        self.color = color
    
    def matrix_point_vgm(self,p,m):
        new_point = [0,0,1]
        new_point[0] = round(p[0]*m[0][0] + p[1]*m[0][1] + new_point[2]*m[0][2],4)
        new_point[1] = round(p[0]*m[1][0] + p[1]*m[1][1] + new_point[2]*m[1][2],4)
        new_point[2] = round(p[0]*m[2][0] + p[1]*m[2][1] + new_point[2]*m[2][2],4)

        return new_point[:2]

    def translate(self,trans_mat):
        p1_h = self.p1[:]
        p2_h = self.p2[:]
    
        self.p1 = self.matrix_point_vgm(p1_h,trans_mat)
        self.p2 = self.matrix_point_vgm(p2_h,trans_mat)

    def draw(self,canvas):
        global height
        global width
        p1 = int(self.p1[0]),int(self.p1[1])
        p2 = int(self.p2[0]),int(self.p2[1])

        cv.circle(canvas,p1,2,self.color,2)
        cv.line(canvas,p1,p2,self.color,2)
        cv.circle(canvas,p2,2,self.color,2)
        return canvas

def create_rot_matrix(angle):
    a = angle
    rot_mat = [
            [ mth.cos(a), -mth.sin(a), 0],
            [ mth.sin(a), mth.cos(a),  0],
            [           0,         0,  1],
        ]
    return rot_mat

def create_transform_matrix(x,y):
    trans_mat = [
                [1,0,x],
                [0,1,y],
                [0,0,1]
            ]
    return trans_mat

class Odometrie:
    def __init__(self,d,pos,ori,color=(255,0,0),vr=0,vl=0):
        self.d = d
        self.pos = pos
        self.ori = ori
        self.vr = vr
        self.vl = vl
        self.color = color
        self.r = 0 if (vr == vl) else (self.d*((vr+vl)/(vr-vl)))
        self.omega = (vr-vl)/(2*self.d)
    



    def berekeningen(self,t,vl,vr):
        self.r = 0 if (vr == vl) else (self.d*((vr+vl)/(vr-vl)))
        self.omega = (vr-vl)/(2*self.d)
        vgem = self.omega*self.r if (vl != vr) else (vl+vr)/2
        self.ori = self.omega*t
        self.pos = int((vgem/self.omega)*mth.sin(self.ori)) if(self.omega != 0) else 0, int((vgem/self.omega)*(mth.cos(self.ori)-1)) if(self.omega != 0) else 0


        
        return vgem, self.ori, self.pos

    def draw(self,canvas):
        global height
        global width
        rotmat = create_rot_matrix(self.ori)
        transmat = create_transform_matrix(width//2,height//2)
        transRmat = create_transform_matrix(-self.r,0)
        lines = [
            Line((0,0),(self.d,0),self.color),
            Line((0,0),(-self.d,0),self.color),
            Line((self.d,-self.d/2),(self.d,self.d/2),self.color),
            Line((-self.d,-self.d/2),(-self.d,self.d/2),self.color),
            Line((0,0),(self.r,0),(0,255,0))

        ]
        for line in lines:
            line.translate(transRmat)
            line.translate(rotmat)
            line.translate(transmat)
            #print(line.p1,line.p2)s
            canvas = line.draw(canvas,)
      

        return canvas




blank = np.zeros((height,width,3),np.uint8)
grid_color = (127,127,127)
for i in range(1,height//gridsize):
    cv.line(blank,(0,i*gridsize),(width,i*gridsize),grid_color,1)
for j in range(1,width//gridsize):
     cv.line(blank,(j*gridsize,0),(j*gridsize,height),grid_color,1)


img_blank = cv.imencode('.png',blank)[1].tobytes()


layout = [ 
    
    [sg.Image(data=img_blank,key='-img-')],
    [
    sg.Column([[ sg.Text('snelheid L')],[
                sg.Slider(range=(-10,10),orientation='h',size=(30,10),key='-VL-',default_value=0),
            ]]),
    sg.VSeparator(),
    sg.Column([[ sg.Text('snelheid R')],[
                sg.Slider(range=(-10,10),orientation='h',size=(30,10),key='-VR-',default_value=0),
            ]]), 
    ],
    [
        sg.HSeparator()
    ],
    [
        sg.Column([[ sg.Text('t')],[
            sg.Slider(range=(0,200),orientation='h',size=(30,10),key='-T-',default_value=0),
        ]])
    ],    
    [
        sg.HSeparator()
    ],
    [
        sg.Column([[ sg.Text('Gem V:')],
                   [ sg.Text("Pos (x,y): ")],
                   [ sg.Text("Orientatie: ")]
                
            ]),
        sg.VSeparator(),
        sg.Column([[ sg.Text('-',key='-vgem-')],
                   [ sg.Text('-',key='-pos-')],
                   [ sg.Text('-',key='-ori-')],
            ]), 
    ]
    ]

window = sg.Window("Odimetrie",layout)

autotje = Odometrie(32,(0,0),0)
t=1

while 1:
    event, values = window.read(timeout=20)
    canvas = blank.copy()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    #cv.imshow('img',canvas)

    vl = values['-VL-']
    vr = values['-VR-']
    t = values['-T-']
    vgem, ori, pos = autotje.berekeningen(t,vl,vr)

    canvas = autotje.draw(canvas)

    window["-img-"].update(data = cv.imencode('.png',canvas)[1].tobytes())
    window["-vgem-"].update(value = str(vgem))
    window["-ori-"].update(value = str(ori))
    window["-pos-"].update(value = f'{pos[0]},{pos[1]}')

       

window.close()
cv.destroyAllWindows()



