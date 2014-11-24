#!/bin/python
#desc:Filter motion detection using a webcam
#package:opencvodos

### Copyright(c) 2014 OpenDomo Services SL. Licensed under GPL v3 or later

import sys
import cv2
import time
import ConfigParser
import numpy as np

ID=sys.argv[1]

config = ConfigParser.ConfigParser()
config.read('/etc/opendomo/vision/filters/' + ID + '/motiondet.conf')
confID = config.get('Definition', 'ID')
confNAME = config.get('Definition', 'NAME')
print confID
print confNAME

imga = cv2.imread('/var/www/data/' + confID + '.jpg')
imgb = cv2.imread('/var/www/data/' + confID + '.jpg')

imgac = cv2.cvtColor(imga, cv2.COLOR_BGR2GRAY)
imgbc = cv2.cvtColor(imgb, cv2.COLOR_BGR2GRAY)

img1 = imgac[10:330, 10:870]
img2 = imgbc[10:320, 10:870]

start = time.clock()
d = cv2.absdiff(img1,img2)
s = d.sum()
t = time.clock() - start
print 'absdiff ', t
print s

start = time.clock()
s = cv2.norm(img1, img2, cv2.NORM_L1)
t = time.clock() - start
print 'norm L1 ',  t
print s
