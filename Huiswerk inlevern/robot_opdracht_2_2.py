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

            lijst[index]._pose[0] = xpos
            lijst[index]._pose[1] = ypos
    
    return lijst

def random_offset(lijst,max_offset):
    lengte_lijst = len(lijst)

    for i in range(lengte_lijst):
        rotatie = random.randrange(0,360)
        offset = random.randrange(0,max_offset*10)/10
        lijst[i].rotate(rotatie)
        lijst[i].forward(offset)
    
    return lijst





robot_lijst = maak_robot_lijst(16)
robot_lijst = maak_grid(robot_lijst,4)
robot_lijst = random_offset(robot_lijst,1)

for i in range(len(robot_lijst)):
    print(robot_lijst[i].get_location(), i + 1)




