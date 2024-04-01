#! /usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):  
    print (msg.ranges[0])
    if msg.ranges[0] < 1:
      #stop turn right
      turn.linear.x = 0
      turn.angular.z = 0
      pub.publish(turn)
      time.sleep(0.5)
      turn.angular.z = 0.5
      pub.publish(turn)
      time.sleep(0.5)
    #mers dreapta
    pub.publish(turn)
    turn.linear.x = 0.5
    pub.publish(turn)



rospy.init_node('scan_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1) 
sub = rospy.Subscriber('/scan', LaserScan, callback) 

rate = rospy.Rate(2)
turn = Twist()

rospy.spin()

