#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import time

from servocntl_pkg import servo

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %f", data.data)
    range = data.data
    dutycycle=2+11*range/255 #my servo runs on inputs from 2 to 13
    test.moveservo(float(dutycycle))
    #time.sleep(1.0)

def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", Float32, callback)

    rospy.spin()

if __name__== '__main__':
    test = servo(description = "test", boardpin = 33, frequency = 50)
    test.setup()

    listener()

