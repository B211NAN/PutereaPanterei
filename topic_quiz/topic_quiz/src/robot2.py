#!/usr/bin/env python

import rospy
from topics_pkg.msg import Age

rospy.init_node('age_publisher')
pub = rospy.Publisher('/RobotAge', Age, queue_size = 1)

rate = rospy.Rate(2)

A = Age()
A.Years = 1
A.Months = 2
A.Days = 3

while not rospy.is_shutdown()
    pub.publish(A)
    rate.sleep()
