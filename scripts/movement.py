#! /usr/bin/env python

import rospy
import sys
from geometry_msgs.msg import Twist
import time
from igvc.msg import pair

pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size = 1)

def callback(data):
    half = data.width // 2
    avg = data.x_avg

    rospy.loginfo("x average is %s",data.x_avg)
    rospy.loginfo("middle pixel at %s",half)

    move = Twist()

    difference_scaling = abs(half-avg)/half
    move.linear.x = 1-(difference_scaling*2)

    #if the midpoint pixel is in left half of screen, rotate the robot right
    if(avg <= half):
        move.angular.z = -2 * (difference_scaling)
    #if the midpoint pixel is in right half of screen, rotate the robot left
    if(avg > half):
        move.angular.z = 2 * (difference_scaling)
        
    pub.publish(move)

def movement():
    rospy.init_node('movement')
    sub = rospy.Subscriber("/avg_and_width", pair, callback)
    rospy.spin()

movement()