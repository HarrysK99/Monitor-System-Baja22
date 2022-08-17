#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from __future__ import print_function
import rospy
import random
from custom_pkg.msg import CarState

def main():
    rospy.init_node('mbed_data_node', anonymous=False)

    pub = rospy.Publisher('carstate', CarState, queue_size=10)

    rate = rospy.Rate(8)

    count = 1

    while not rospy.is_shutdown():
    	temp_1=random.randrange(1,100)
    	temp_2=random.randrange(1,100)
    	temp_3=random.randrange(1,100)
    	temp_4=random.randrange(1,100)
    	
    	sig = CarState()
        
    	sig.f_wheel_velocity_FL_ms=temp_1
    	sig.f_wheel_velocity_FR_ms=temp_1
    	sig.f_wheel_velocity_RL_ms=temp_1
    	sig.f_wheel_velocity_RR_ms=temp_1
        
    	sig.f_car_velocity_ms=temp_2
    	sig.i_throttle=temp_3
        
    	sig.f_motor_torque_FL_Nm=temp_4
    	sig.f_motor_torque_FR_Nm=temp_4
    	sig.f_motor_torque_RL_Nm=temp_4
    	sig.f_motor_torque_RR_Nm=temp_4
        
    	sig.c_torque_mode_flag=1
    	sig.c_motor_mode_flag[0]=1
    	sig.c_motor_mode_flag[1]=1
    	sig.c_motor_mode_flag[2]=1
    	sig.c_motor_mode_flag[3]=1
        
    	pub.publish(sig)
        
    	rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
