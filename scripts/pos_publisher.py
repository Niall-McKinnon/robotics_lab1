#!/usr/bin/env python3

import rospy

# we are going to read turtlesim/Pose messages here
from turtlesim.msg import Pose

# Import twist
from geometry_msgs.msg import Twist

# import the new shortpose message
from robotics_lab1.msg import Turtlecontrol

import math

# create global variables
xd = 0.0
kp = 0.0
xt = 0.0
velocity = 0.0

def control_params_callback(data):
	
	global xd
	global kp
	
	# Get control parameters from turtlecontrol.msg
	xd = data.xd
	kp = data.kp
	
	# show the results on screen
	rospy.loginfo('xd is %0.2f, kp is %0.2f', xd, kp)
	
def pose_callback(data):
	
	global xt
	
	# Get currentx position of turtle
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
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	
	# Initialize Twist variable
	vel_cmd = Twist()
	
	# set a 10 Hz frequency for the publisher loop
	loop_rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		
		# Calculate velocity based on turtle location:
		vel_cmd.linear.x = kp * (xd - xt)
		
		# Publish the message
		cmd_pub.publish(vel_cmd)
		
		# We pause/sleep here for 0.1 of a second
		loop_rate.sleep()
