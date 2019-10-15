#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import board
import busio
from servocntl_pkg import servo

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %f", data.data)
    range=data.data
    dutycycle = 2+11*range/255
    dutycycle = round(dutycycle, 2)
    test.moveservo(float(dutycycle))
    time.sleep(1.0)
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    test = servo(description = "test", boardpin = 33, frequency = 50)
    test.setup()
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("ece4422/motorcontrol", Float32, callback)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()


###############

