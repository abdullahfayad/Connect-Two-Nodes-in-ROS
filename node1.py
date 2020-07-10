#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('hello', String, queue_size=10) #'hello' is the topic name
	rospy.init_node('node1') #'node1' is name of the node
	rate = rospy.Rate(5) #5 times/second
	while not rospy.is_shutdown():
		x = "Hello, Abdullah"
		rospy.loginfo(x)
		pub.publish(x)
		rate.sleep()

if __name__ == '__main__':
	print ("I am node 1")
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
