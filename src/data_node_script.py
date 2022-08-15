#!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import print_function
import rospy
import random
from custom_msg2_pkg.msg import CarSignal, CarState, CarControlSignal

def main():
    rospy.init_node('data_node', anonymous=False)

    pub = rospy.Publisher('signals', CarSignal, queue_size=10)

    rate = rospy.Rate(8)

    count = 1

    while not rospy.is_shutdown():
    	temp_1=random.randrange(1,100)
    	temp_2=random.randrange(1,100)
    	temp_3=random.randrange(1,100)
    	temp_4=random.randrange(1,100)
    	
    	
    	sig = CarSignal()
        
    	sig.state.f_wheel_velocity_FL_ms=temp_1
    	sig.state.f_wheel_velocity_FR_ms=temp_1
    	sig.state.f_wheel_velocity_RL_ms=temp_1
    	sig.state.f_wheel_velocity_RR_ms=temp_1
        
    	sig.state.f_car_velocity_ms=temp_3
        
    	sig.state.f_motor_torque_FL_ms=temp_4
    	sig.state.f_motor_torque_FR_ms=temp_4
    	sig.state.f_motor_torque_RL_ms=temp_4
    	sig.state.f_motor_torque_RR_ms=temp_4
        
    	sig.controlSignal.brake=temp_2
    	sig.controlSignal.steering=temp_2
    	sig.controlSignal.acceleration=temp_2
       
       
    	print("temp_1=",temp_1)
    	print("temp_2=",temp_2)
    	print("temp_3=",temp_3)
    	print("temp_4=",temp_4)
        
    	pub.publish(sig)
        
    	rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
