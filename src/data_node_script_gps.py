#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from __future__ import print_function
import rospy
from sensor_msgs.msg import NavSatFix

def main():
	rospy.init_node('gps_data_node',anonymous=False)

	pub=rospy.Publisher('ublox_gps/fix', NavSatFix, queue_size=3)

	rate=rospy.Rate(8)

	while not rospy.is_shutdown():
		sig=NavSatFix()
		sig.latitude=35.9476231
		sig.longitude=126.5924496

		pub.publish(sig)

		rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
