#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
import matplotlib.pyplot as plt

point = Point()
rospy.init_node('detect_cans_node', anonymous=True)


def callback(msg):
    global point
    point=msg.pose.pose.position
    return(msg.pose.pose.position)


class LoadFeature(object):

    def __init__(self):
    
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.camera_callback)
        self.bridge_object = CvBridge()
        self.odom_sub = rospy.Subscriber('/odom', Odometry, callback)
        self.pub = rospy.Publisher('/bottle', Point, queue_size=1)

    def camera_callback(self,data):
        try:
            # We select bgr8 because its the OpenCV encoding by default
            cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
        except CvBridgeError as e:
            print(e)

        hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        h,s,v= cv2.split(hsv)
        _, th_h_low = cv2.threshold(h,20,255,cv2.THRESH_BINARY_INV)
        _, th_h_high = cv2.threshold(h,160,255,cv2.THRESH_BINARY)
        th_h = th_h_low|th_h_high
        _, th_s = cv2.threshold(s,100,255,cv2.THRESH_BINARY)
        th_red = th_h & th_s

        _, contours, hierarchy = cv2.findContours(th_red,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:

            # find the biggest countour (c) by the area
            c = max(contours, key = cv2.contourArea)
            x,y,w,h = cv2.boundingRect(c)
            if(h>150):
                self.pub.publish(point)
            # draw the biggest contour (c) in green
            cv2.rectangle(cv_image,(x,y),(x+w,y+h),(0,255,0),2)


        cv2.imshow('th_h',th_h)

        cv2.imshow('th_s',th_s)

        cv2.imshow('th_red',th_red)

        cv2.imshow('Camera',cv_image)       

        cv2.waitKey(1)

def main():
    load_feature_object = LoadFeature()
    
    try:
        rospy.spin()
        
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()