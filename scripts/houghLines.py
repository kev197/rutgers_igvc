#!/usr/bin/env python
from __future__ import print_function

import roslib
roslib.load_manifest('igvc')
import sys
import rospy
import numpy as np
import cv2
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from igvc.msg import pair
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from heapq import heapify, heappush, heappop 

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("/image_raw",Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/image_raw",Image,self.callback)
    self.x_avg_pub = rospy.Publisher("/avg_and_width", pair, queue_size=10)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

    except CvBridgeError as e:
      print(e)

    grayImage = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

    # blurs the image
    blur = cv2.GaussianBlur(grayImage, (7, 7), 0)

    #apply canny edge 
    v = np.median(grayImage)
    sigma = 0.33
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edge = cv2.Canny(grayImage, lower+3000, upper+3000, apertureSize = 5)

    #dilate the edges
    kernel = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(edge,kernel,iterations = 1)

    (h,w) = cv_image.shape[:2]

    #shrinks region of interest horizontally
    scale = (h//5)+100
    # shrinks region of interest vertically
    widthScale = 200


    # crops image to fit a "region of interest"
    cropped_image = dilation[scale:(h-scale-100), widthScale:(w-widthScale)]
    # cv2.imshow("region of interest", cropped_image)


    # 720x1080 -> 360x1080 (bottom half of image)

    #lines is an array of lines generated from cropped_image, using hough lines
    lines = cv2.HoughLinesP(cropped_image, 1, np.pi / 180, 20, minLineLength = 150, 
    maxLineGap = 200)

    x1_left = h
    x1_right = 0
    x2_left = h
    x2_right = 0
    y1_left = h
    y1_right = 0
    y2_left = h
    y2_right = 0

    # go through each line (the line is a line segment from (x1,y1) to (x2,y2))
    for cur in lines:
        x1 = cur[0][0]
        y1 = cur[0][1]
        x2 = cur[0][2]
        y2 = cur[0][3]

        # takes the leftmost line
        if x1 < x1_left and x2 < x2_left:
            y1_left = y1
            y2_left = y2
            x1_left = x1
            x2_left = x2
        # takes the rightmost line
        elif x1 > x1_right and x2 > x2_right:
            y1_right = y1
            y2_right = y2
            x1_right = x1
            x2_right = x2


    # print the coordinates of the left and right bounding lines
    # print("\n\n-right-bound-\n")
    # print("({}, {}) - ({}, {})".format(x1_right, y1_right, x2_right, y2_right))
    # print("\n\n-left-bound-\n")
    # print("({}, {}) - ({}, {})".format(x1_left, y1_left, x2_left, y2_left))

    #puts the leftbound, rightbound lines on cv_image
    cv2.line(cv_image, (x1_right+widthScale, y1_right+scale), (x2_right+widthScale, y2_right+scale), (0, 0, 255), 12)
    cv2.line(cv_image, (x1_left+widthScale, y1_left+scale), (x2_left+widthScale, y2_left+scale), (0, 0, 255), 12)


    # calculates a midpoint line and puts it on cv_image
    x1_avg = int((x2_right + x1_left) / 2)
    y1_avg = int((y1_right + y1_left) / 2)
    x2_avg = int((x1_right + x2_left) / 2)
    y2_avg = int((y2_right + y2_left) / 2)

    # cv2.line(cv_image, (x1_avg+widthScale, h), (x2_avg+widthScale, scale), (255, 0, 0), 30)

    # Making a heap. The heap will be used to store all the x-coordinates of
    # obstacles/potholes/lanes. We will calculate the largest gap between any two 
    # of these, and place the "midpoint" (where our robot goes) between the two

    # Creating empty heap 
    heap = [] 
    heapify(heap) 
      
    # Adding items to the heap using heappush function 
    heappush(heap, [(x1_left+x2_left)/2, (y1_left+y2_left)/2]) 
    heappush(heap, [(x1_right+x2_right)/2, (y1_right+y2_right)/2]) 
      

    # detects the orange cones. Puts x values in keypoints array, of type KeyPoint
    cropped_image_original = cv_image[(scale+100):(h-scale+200), widthScale:(w-widthScale)]
    hsv = cv2.cvtColor(cropped_image_original, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,(5, 50, 50), (15, 255, 255) )
    params = cv2.SimpleBlobDetector_Params()
    params.filterByArea = False
    params.minArea = 1
    params.filterByCircularity = False
    params.filterByConvexity = False
    params.filterByInertia = False
    detector = cv2.SimpleBlobDetector_create(params)
    inverted_img = cv2.bitwise_not(mask)
    keypoints = detector.detect(inverted_img)
    for point in keypoints:
      # print("x is\n")
      # print("{}".format(point.pt[0]) + "\n")
      heappush(heap, [point.pt[0], point.pt[1]])

    # this code just rescales the detected points to the original image, then 
    # displays it on cv_image
    for point in keypoints:
      point.pt = (point.pt[0]+widthScale, point.pt[1]+scale+130)
    draw_keypoints(cv_image, keypoints, (20, 255, 100))

    avg_x1_x2 = 0
    biggest_gap = 0
    (h_cropped,w_cropped) = cropped_image_original.shape[:2]

    #calculate midpoint based on obstacles and lanes in the heap
    while len(heap) != 1:
      removed = heappop(heap)
      current = heap[0]
      difference = current[0] - removed[0]
      if difference > biggest_gap:
        biggest_gap = difference
        # if the left obstacle is a lane and the right obstacle is a barrel:


        # ---------experimental turning ----------------#

        # if the left obstacle is a lane and the right obstacle is a barrel:
        if removed[0] == (x1_left+x2_left)/2 and current[0] != (x1_right+x2_right)/2:
          #shift the midpoint left
          avg_x1_x2 = int(removed[0] + (difference / 2) - 110*(current[1]/h_cropped))
          print("the shifted midpoint is {}".format(avg_x1_x2) + "\n")
          # print("the normal midpoint is {}".format(int(removed[0] + (difference / 2))) + "\n")
        # if the right obstacle is a lane and the left obstacle is a barrel:
        elif removed[0] != (x1_left+x2_left)/2 and current[0] == (x1_right+x2_right)/2:
          #shift the midpoint right
          avg_x1_x2 = int(removed[0] + (difference / 2) + 110*(removed[1]/h_cropped))
          # print("{}".format(200*(removed[1]/h_cropped)) + "\n")
        else:
          avg_x1_x2 = int(removed[0] + (difference / 2))

        # ---------experimental turning ----------------#

        # avg_x1_x2 = int(removed[0] + (difference / 2))


    cv2.circle(cv_image, (avg_x1_x2+widthScale, h//2), 10, (255,0,0), thickness=-1)

    # publish a pair (/igvc/msg/pair) to the avg_and_width topic
    # This holds the midpoint pixelx and pixel width of camera
    # This data is used to align robot with midpoint line
    pubPair = pair()
    pubPair.x_avg = avg_x1_x2 + widthScale
    pubPair.width = w
    self.x_avg_pub.publish(pubPair)

    # cv2.imshow("blobs", img_with_keypoints)
    cv2.imshow("result", cv_image)
    cv2.waitKey(10)

def draw_keypoints(img, keypoints, color):
    for kp in keypoints:
        x, y = kp.pt
        cv2.circle(img, (int(x), int(y)), color=color, radius=10, thickness=-1) # you can change the radius and the thickness

def main(args):
  ic = image_converter()
  rospy.init_node('image_converter')
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)