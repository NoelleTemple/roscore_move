#!/usr/bin/env python
   # license removed for brevity
import rospy
from std_msgs.msg import Float32
import logging
import time
from rpisensors.proximity import VL6180X
from rpisensors.proximity import VL_ALS_GAIN_20

def talker():
    pub = rospy.Publisher('/ece4422/motorcontrol', Float32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    sensor = VL6180X(1)
    while not rospy.is_shutdown():
        range = sensor.read_distance()
        data=range
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
