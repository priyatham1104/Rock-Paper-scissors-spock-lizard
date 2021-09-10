#!/usr/bin/env python
# coding: utf-8

# In[ ]:


######### Squeeze net ############
# 1) Collecting an image dataset
# 2) Squeeze Net (only retraining the final layers)
# 3) Training
# 4) Testing
# 5) Make somthing intersting out of it


# In[ ]:


############# Gather Images #############


# In[1]:


import cv2
import os
from os import path
import sys


# In[2]:


dir0 = os.getcwd()
print(dir0)
dir_img = dir0 + "\\images"
print(dir_img)


# In[10]:


def get_images(name):
    os.chdir(dir_img)
    try:
        os.mkdir(name)
    except:
        print("Couldn't make a directory")
    img_counter = 0
    dir_new = dir_img + name
    os.chdir(name)
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)
        cv2.rectangle(frame, (0,0), (1000,1000), (255,255,255), 2)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            roi = frame[100:500, 100:500]
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, roi)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()
    os.chdir(dir0)


# In[11]:


get_images("dog")


# In[ ]:




