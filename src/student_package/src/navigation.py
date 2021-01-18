#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

twist = Twist()

def callback(msg): 
    front_distance=msg.ranges[360]
    right_distance=msg.ranges[0]
    left_distance=msg.ranges[719]
    if front_distance>1: #wall far away:
        twist.linear.x=0.5 # move straight forward
        twist.angular.z=0
    else:
        twist.angular.z=-1.5 #turn left by default
        if right_distance<1: #if wall on the right, stop and continue to turn left
            twist.linear.x=0
        if left_distance<1: #if wall on the left, stop and turn instead
            twist.linear.x=0
            twist.angular.z=1.5
    pub.publish(twist)


rospy.init_node('topics_quiz_node')
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.spin()