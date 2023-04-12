#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:08:38 2022

@author: beste
"""

import rospy
from geometry_msgs.msg import Twist

def ilerleme():
    rospy.init_node("duz_git")
    pub = rospy.Publisher("cmd_vel",Twist, queue_size=10)
    hiz_mesaji = Twist
    hiz_mesaji.linear.x = 0.5
    mesafe = 5
    yer_degiştirme = 0
    t0 = rospy.Time.now.to_sec
    while (yer_degiştirme < mesafe):
        pub.publish(hiz_mesaji)
        t1=rospy.Time.now.to_sec
        yer_degiştirme = hiz_mesaji.linear.x * (t1-t0)
    hiz_mesaji.linear.x = 0
    pub.publish(hiz_mesaji)
    rospy.loginfo(hiz_mesaji)
ilerleme()


        
    