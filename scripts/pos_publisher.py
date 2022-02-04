#!/usr/bin/env python3

import rospy

# we are going to read turtlesim/Pose messages here
from turtlesim.msg import Pose

from geometry_msg.msg import Twist

# import the new shortpose message
from robotics_lab1.msg import Turtlecontrol

# for converting radians to degrees, import the math module
import math

# Declare a constant for the angular position scales
# ROTATION_SCALE = 180.0/math.pi

pos_msg = Turtlecontrol()

xd = 0.0
kp = 0.0
xt = 0.0
velocity = 0.0

def control_params_callback(data):
	#global pos_msg
	
	# Get turtle's x possition:
	global xd
	# Get the turtle's desired position:
	global kp
	
	xd = data.xd
	kp = data.kp
	
	
	# Calculate velocity based on turtle location:
	
	
	# show the results on screen
	rospy.loginfo('xd is %0.2f, kp is %0.2f', xd, kp)
	
def pose_callback(data):
	
	# convert x and y to cm
	global xt
	
	xt = data.x
	

if __name__ == '__main__':
	# initialize the node
	rospy.init_node('pos_publisher', anonymous = True)
	
	# add a subscriber to read position information fromn turtle1/pos
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	rospy.Subscriber('/turtle1/control_params', Turtlecontrol, control_params_callback)
	
	# spin() simply keeps python from exiting until this node is stopped
	# rospy.spin()
	
	# define a publisher
	pos_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	
	# set a 10 Hz frequency for the publisher loop
	loop_rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
	
		velocity = kp * (xd - xt)
		
		# Publish the message
		pos_pub.publish(pos_msg)
		
		# We pause/sleep here for 0.1 of a second
		loop_rate.sleep()
