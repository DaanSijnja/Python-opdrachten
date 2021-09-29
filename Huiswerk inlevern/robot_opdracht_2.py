"""
Definition of the Robot class used for simulating the pose (location and orientation) 
of a robot in 2D.
For use in the practical ModProg, Mechatronics programme, The Hague University of Applied
Sciences.
Creation date: 25/08/2021
License: GNU General Public License (GNU GPLv3)
"""
import math as m
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
        
        next_x = distance*m.cos(self.get_orientation()*(m.pi/180))
        next_y = distance*m.sin(self.get_orientation()*(m.pi/180))

        self._pose[0] += round(next_x,2)
        self._pose[1] += round(next_y,2)

        

    def rotate(self, angle = 0.0):
        """Changes the orientation only, i.e. adds angle to the orientation."""
        self._pose[2] += angle

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

        distance = m.sqrt((diff_x)**2+(diff_y)**2)

        return round(distance,2)
 

def distance_between_robots(robot1,robot2):
        diff_x = robot1.get_x() - robot2.get_x()
        diff_y = robot1.get_y() - robot2.get_y()

        distance = m.sqrt((diff_x)**2+(diff_y)**2)

        return round(distance,2)
 

def geef_locatie(lijst):
    lengte_lijst = len(lijst)
    zijde = round(m.sqrt(lengte_lijst))

    index = 0

    for i in range(zijde):

        for j in range(zijde):
            lijst[index]._pose[0] = i*10 - 50
            lijst[index]._pose[1] = j*10 - 50
            index += 1

def maak_lijst(lijst_grote):
    robot_lijst = []
    for i in range(lijst_grote):
        robot_i = Robot()
        robot_lijst.append(robot_i)
    
    geef_locatie(robot_lijst)

    return robot_lijst





robot_lijst = maak_lijst(100)

for i in range(len(robot_lijst)):
    print(robot_lijst[i]._pose)



