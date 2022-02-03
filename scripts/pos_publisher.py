#!/usr/bin/env python3

import rospy

# we are going to read turtlesim/Pose messages here
from turtlesim.msg import Pose

# import the new shortpose message
from robotics_lab1.msg import Turtlecontrol

# for converting radians to degrees, import the math module
import math

# Declare a constant for the angular position scales
ROTATION_SCALE = 180.0/math.pi

pos_msg = Turtlecontrol()

def pose_callback(data):
	global pos_msg
	
	# convert angular positions to degrees
	pos_msg.theta = data.theta * ROTATION_SCALE
	
	# convert x and y to cm
	pos_msg.x = data.x * 100
	pos_msg.y = data.y * 100
	
	# show the results on screen
	# rospy.loginfo('x is %0.2f cm, y is %0.2f cm, theta is %0.2f degrees', x_in_cm, y_in_cm, rot_in_degrees)
	

if __name__ == '__main__':
	# initialize the node
	rospy.init_node('pos_publisher', anonymous = True)
	
	# add a subscriber to read position information fromn turtle1/pos
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	
	# spin() simply keeps python from exiting until this node is stopped
	# rospy.spin()
	
	# define a publisher
	pos_pub = rospy.Publisher('/turtle1/shortpose', Shortpose, queue_size = 10)
	
	# set a 10 Hz frequency for the publisher loop
	loop_rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		# Publish the message
		pos_pub.publish(pos_msg)
		
		# We pause/sleep here for 0.1 of a second
		loop_rate.sleep()
