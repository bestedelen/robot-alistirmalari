#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 13:07:58 2022

@author: beste
"""

import rospy
from basit_uygulamalar.srv import CemberHareket
rospy.wait_for_service("cember_servis)
 try:
     yaricap=float(input("yaricap giriniz:))
     servis = rospy.ServiceProxy("cember_servis",CemberHareket)
     servis(yaricap)
except rospy.ServiceException:
    print("servisle alakalı hata meydana geldi")
    