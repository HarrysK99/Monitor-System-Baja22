#!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import print_function
import rospy				
from custom_msg2_pkg.msg import CarSignal, CarState, CarControlSignal


def points_topic_callback(data):
    print(data.state.f_wheel_velocity_FL_ms)
    print(data.controlSignal.brake)
    print(data.state.f_car_velocity_ms)
    print(data.state.f_motor_torque_FL_ms)
    
def main():
    rospy.init_node('print_node', anonymous=False)
    #rospy.Subscriber('signals', CarSignal, points_topic_callback)
    rospy.Subscriber('data',CarSignal,points_topic_callback)

    rospy.spin()

if __name__ == '__main__':
    main()
