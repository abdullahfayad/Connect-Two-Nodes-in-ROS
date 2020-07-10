#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
	rospy.loginfo("I heard %s",data.data)

def listener():
	rospy.init_node('node2') #'node2' is name of the node
	rospy.Subscriber('hello', String, callback) #'hello' is the topic name and it should be the same as the sender topic name
	rospy.spin()

if __name__ == '__main__':
	print ("I am node 2")
	listener()
