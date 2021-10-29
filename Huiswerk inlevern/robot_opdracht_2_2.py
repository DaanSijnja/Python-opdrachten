"""
Definition of the Robot class used for simulating the pose (location and orientation) 
of a robot in 2D.
For use in the practical ModProg, Mechatronics programme, The Hague University of Applied
Sciences.
Creation date: 25/08/2021
License: GNU General Public License (GNU GPLv3)
"""
import math 
import random
import time

import matplotlib.pyplot as plt
import numpy as np


class Robot:
    """Robot class for 2D robot objects."""

    def __init__(self, pose = None):
        """
        Robot(pose) returns a Robot object where pose is a
        list of three numbers, the first two are the Robot's
        x- and y-coordinate, the third value is the orientation.
        Robot() will return a Robot object with its pose set to
        the default value [0.0, 0.0, 0.0].
        """
        if pose is None:
            pose = [0.0, 0.0, 0.0]
            
        self._pose = pose  # attributes with 1 or 2 underscores (_)
        # before its name are meant in python not to be used from outside the class
        # definition, so are internal to the class. Sometimes called private, but they
        # are not secret.

    def get_pose(self):
        """Returns the pose of the robot."""
        return self._pose

    def set_pose(self, pose = None):
        """Sets the pose of the robot, without argument
        the pose is set to its default value [0.0, 0.0, 0.0]."""
        if pose is None:
            pose = [0.0, 0.0, 0.0]
        self._pose = pose

    def get_location(self):
        """Returns the location of the robot in 2D (first x-, then y-coordinate)."""
        return self._pose[0:2]

    def get_x(self):
        """Returns the x-coordinate of the robot."""
        return self._pose[0]

    def get_y(self):
        """Returns the y-coordinate of the robot."""
        return self._pose[1]

    def get_orientation(self):
        """Returns the orientation of the robot in radians."""
        return self._pose[2]

    def forward(self, distance = 0.0):
        """Moves the robot over a distance in the direction of its
        current orientation."""
        x = distance*math.cos(self.get_orientation())
        y = distance*math.sin(self.get_orientation())
    	
        self._pose[0] += round(x,1)
        self._pose[1] += round(y,1)
        
    def rotate(self, angle = 0.0):
        """Changes the orientation only, i.e. adds angle to the orientation."""
        self._pose[2] += round(angle*(math.pi/180),2)

    def move(self, distance = 0.0, angle = 0.0):
        """First moves in a straight line over distance and then
        adds angle to its orientation."""
        self.forward(distance)
        self.rotate(angle)

    def distance_to(self, other_robot):
        """
        Calculates the distance of the robot to other_robot.
        """
        diff_x = other_robot.get_x() - self.get_x()
        diff_y = other_robot.get_y() - self.get_y()

        return math.sqrt(diff_x**2 + diff_y**2)


def distance_between_two_robots(r_1,r_2):
 
    diff_x = r_1.get_x() - r_2.get_x()
    diff_y = r_1.get_y() - r_2.get_y()

    return math.sqrt(diff_x**2 + diff_y**2)

def maak_robot_lijst(aantal_robots):
    lijst = []

    for i in range(aantal_robots):
        robot_i = Robot()
        lijst.append(robot_i)

    return lijst

def maak_grid(lijst,distance):
    lengte_lijst = len(lijst)
    lengte_zijde = math.ceil(math.sqrt(lengte_lijst))

    for i in range(lengte_lijst):
        for j in range(lengte_zijde):
            index = (i * lengte_zijde + j)

            if(index > (lengte_lijst-1)):
                break

            xpos = j * distance - ((lengte_zijde - 1) / 2) * distance 
            ypos = ((lengte_zijde - 1 ) / 2 ) * distance - i * distance

            lijst[index]._pose[0] = round(xpos,1)
            lijst[index]._pose[1] = round(ypos,1)
    
    return lijst

def random_offset(lijst,max_offset):
    lengte_lijst = len(lijst)

    for i in range(lengte_lijst):
        rotatie = random.randrange(0,360)
        offset = random.randrange(0,max_offset*10)/10
        lijst[i].rotate(rotatie)
        lijst[i].forward(offset)
    
    return lijst

def print_lijst(lijst,aantal = None):
    lengte_lijst = len(lijst)

    if(aantal == None or aantal > lengte_lijst):
        aantal = lengte_lijst

    for i in range(aantal):
        print('x: ' + str(round(lijst[i].get_pose()[0],1)) ,'y: ' + str(round(lijst[i].get_pose()[1],1)),'d: ' + str(round(lijst[i].get_pose()[2],1)), ' robot: ', i + 1)

def move_robots(lijst,distance, orientation):
    lengte_lijst = len(lijst)

    for i in range(lengte_lijst):
        lijst[i].move(distance,orientation)

    return lijst


#dit werkt niet want het word pas op het laatst geupdate
def move_over_given_time(lijst,max_offset,max_time):
    lengte_lijst = len(lijst)

    for h in range(max_time):
        print( str(h+1) + '/' + str(max_time) + ' seconden')
        for i in range(lengte_lijst):   
            rotatie = random.randrange(0,360)
            offset = random.randrange(0,max_offset*10)/10
            lijst[i].move(offset,rotatie)
        print_lijst(lijst,10)
        time.sleep(1)

    return lijst




def numpy_naar_quiver(lijst):
    '''numpy3d naar quiver coordinaten voor de mathplotlib'''
    x,y,u,v = [],[],[],[]
    
    for i in range(len(lijst)):
        x.append(lijst[i][0])
        y.append(lijst[i][1])
        u.append(lijst[i][2])
        v.append(lijst[i][3])

    quiver_lijst = np.array([x,y,u,v])
    return quiver_lijst



def numpy_3d(robot_lijst,seconden):
    '''in deze functie maken we een lijst van de robots en verplaatsen we deze ook'''
    lengte_robot_lijst = len(robot_lijst)
    numpy_3d_array = []

    for tijdstip in range(seconden):
        t = []
        for robot in range(lengte_robot_lijst):
            X = robot_lijst[robot].get_x()
            Y = robot_lijst[robot].get_y()
            U = math.cos(robot_lijst[robot].get_orientation())
            V = math.sin(robot_lijst[robot].get_orientation())
            
            t.append([X,Y,U,V])
            robot_lijst[robot].forward(0.1)
        numpy_3d_array.append(t)

    numpy_3d_array = np.asarray(numpy_3d_array)
    return robot_lijst, numpy_3d_array

def doe_berekening_op_lijst(lijst,functie):
    '''hier mag je alleen de np.std en de np.mean functie in stoppen'''
    X_berekend = functie(lijst[0])
    Y_berekend = functie(lijst[1])
    U_berekend = functie(lijst[2])
    V_berekend = functie(lijst[3])
    uitkomst_array = np.array([X_berekend,Y_berekend,U_berekend,V_berekend])
    return uitkomst_array


SEC = 20
robot_lijst = maak_robot_lijst(100)
robot_lijst = maak_grid(robot_lijst,1)
robot_lijst = random_offset(robot_lijst,0.1)

robot_lijst, numpy3d = numpy_3d(robot_lijst,SEC)



plt.ion()
fig, ax = plt.subplots()
plt.show()

for tijdstip in range(SEC):
    quiver_array = numpy_naar_quiver(numpy3d[tijdstip])
    print( str(tijdstip+1) + '/' + str(SEC) + ' seconden')
    mean = doe_berekening_op_lijst(quiver_array,np.mean)
    st_deviatie = doe_berekening_op_lijst(quiver_array,np.std)

    print(f'Gemiddelde: X:{round(mean[0],2)} Y:{round(mean[1],2)} U: {round(mean[2],2)} V:{round(mean[3],2)}')
    print(f'Standaard Deviatie: X:{round(st_deviatie[0],2)} Y:{round(st_deviatie[1],2)} U: {round(st_deviatie[2],2)} V:{round(st_deviatie[3],2)}')
    
    q = ax.quiver(quiver_array[0], quiver_array[1], quiver_array[2], quiver_array[3])
    ax.quiverkey(q, X=0.3, Y=1.1, U=10, label=('tijd: ' + str(tijdstip) + 'sec'), labelpos='E')

    fig.canvas.draw()  
    plt.pause(0.1)  
    ax.cla() 
    time.sleep(1)



