#!/usr/bin/env python3

import rospy

# we are going to read turtlesim/Pose messages here
from turtlesim.msg import Pose

# for converting radians to degrees, import the math module
import math



def pose_callback(data):
	
	# convert x and y to cm
	x_in_cm = data.x * 100
	y_in_cm = data.y * 100
	
	# show the results on screen
	rospy.loginfo('x is %0.2f cm, y is %0.2f cm, theta is %0.2f degrees', x_in_cm, y_in_cm, rot_in_degrees)
	

if __name__ == '__main__':
	# initialize the node
	rospy.init_node('pos_converter', anonymous = True)
	
	# add a subscriber to read position information fromn turtle1/pos
	rospy.Subscriber('/turtle1/control_params', Pose, pose_callback)
	
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
