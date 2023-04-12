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

message_1=String()
message_2=String()
message_3=String()
message_4=String()

while not rospy.is_shutdown():
    
    
    message_1.data="Ben Beste"
    message_2.data="Ben Bd"
    message_3.data="Ben B"
    message_4.data="Ben D"
    
    pub_1.publish(message_1)
    pub_2.publish(message_2)
    pub_3.publish(message_3)
    pub_4.publish(message_4)
    
    rate.sleep()
    rospy.loginfo("node durduruldu.")

    