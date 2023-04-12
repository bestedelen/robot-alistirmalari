#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 20:17:57 2022

@author: beste
"""

import rospy
from std_msgs.msg import String


rospy.init_node("verici")
pub_1=rospy.Publisher("yayinci_1",String,queue_size=10)
pub_2=rospy.Publisher("yayinci_2",String,queue_size=10)
pub_3=rospy.Publisher("yayinci_3",String,queue_size=10)
pub_4=rospy.Publisher("yayinci_4",String,queue_size=10)                   
                        
rate=rospy.Rate(1)
    
while not rospy.is_shutdown():
    message=String()
    message.data="Ben Beste"
    message.data="Ben Bd"
    message.data="Ben B"
    message.data="Ben D"
    pub_1.publish(message)
    pub_2.publish(message)
    pub_3.publish(message)
    pub_4.publish(message)
    rate.sleep()
    rospy.loginfo("node durduruldu.")

    