#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
    # Overwrite header timestamp with current time
    msg.header.stamp = rospy.Time.now()
    fixed_pub.publish(msg)

rospy.init_node('laser_timestamp_fixer')
fixed_pub = rospy.Publisher('/scan_fixed', LaserScan, queue_size=10)
rospy.Subscriber('/scan', LaserScan, scan_callback)
rospy.spin()