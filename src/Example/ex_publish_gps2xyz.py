#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from __future__ import print_function
import rospy
from sensor_msgs.msg import NavSatFix

def main():
	rospy.init_node('gps_data_node',anonymous=False)

	pub=rospy.Publisher('ublox_gps/fix', NavSatFix, queue_size=3)

	rate=rospy.Rate(8)
	#37.541739, 127.079558
	#37.541451, 127.079519
	sig=NavSatFix()
	sig.latitude=37.541451
	sig.longitude=127.079519
	
	count=0	
	
	while not rospy.is_shutdown():
		#count+=1
		
		#if count==8 : 
		count=0
		sig.latitude+=0.000288
		sig.longitude+=0.000039

		pub.publish(sig)

		rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
