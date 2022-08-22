#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys
import time
import rospy

from driver_system.msg import CarState
from sensor_msgs.msg import NavSatFix
from driver_system.msg import DrivingData

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets

global RGB_CONST
RGB_CONST=32

global START_POINT
START_POINT=[37.5418547, 127.07906279999999] #[0]: latitude, [1]: longitude

global START_WIDTH
START_WIDTH=[0.00002, 0.00006]

global MAX_LAP
MAX_LAP=30

global mbed_flag
mbed_flag=0

global GPS_flag
GPS_flag=0

#UI파일 연결
#UI파일과 py코드 파일은 같은 디렉토리에 위치
form_class = uic.loadUiType("./ui/driverMonitorUi.ui")[0]

#publisher & message
pub=rospy.Publisher('driving_data', DrivingData, queue_size=1)
pub_msg=DrivingData()

#Mbed Communicate
class CommunicateFromMbed(QObject):
    signal=pyqtSignal(CarState)

    def run(self,data):
        self.signal.emit(data)

#GPS Communicate
class CommunicateFromGPS(QObject):
    signal=pyqtSignal(NavSatFix)

    def run(self,data):
        self.signal.emit(data)

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.mbed_trigger=CommunicateFromMbed()
        self.GPS_trigger=CommunicateFromGPS()

        self.mbed_trigger.signal.connect(self.SettingByMbed)
        self.GPS_trigger.signal.connect(self.SettingByGPS)

        #self.mbed_flag=0
        #self.GPS_flag=0
        self.start_time_ref=0
        self.total_time_ref=0
        self.lap=0
        self.lap_percent=0
        self.start_flag=0
        self.lap_time_ref=0
        self.start_duration=0
        self.total_duration=0
        self.lap_time_cur="00:00:00"
        self.lap_time_prev="00:00:00"
        self.total_time="00:00:00"

    def emitSignalFromMbed(self,data):
        self.mbed_trigger.run(data)
    
    def emitSiganlFromGPS(self,data):
        self.GPS_trigger.run(data)
    
    # Mbed 통신 Slot 함수
    @pyqtSlot(CarState)
    def SettingByMbed(self,data):
        _translate = QtCore.QCoreApplication.translate
        global RGB_CONST
        global pub, pub_msg
        global mbed_flag, GPS_flag
        #print('SettingByMbed')

        # flag check and publish
        if (mbed_flag==1 and GPS_flag==1):
            print('mbed_pub')
            pub.publish(pub_msg)
            mbed_flag=0
            GPS_flag=0

        # Setting publish msg 
        pub_msg.f_motor_torque_FL_Nm=data.f_motor_torque_FL_Nm
        pub_msg.f_motor_torque_FR_Nm=data.f_motor_torque_FR_Nm
        pub_msg.f_motor_torque_RL_Nm=data.f_motor_torque_RL_Nm
        pub_msg.f_motor_torque_RR_Nm=data.f_motor_torque_RR_Nm
        pub_msg.f_wheel_velocity_FL_ms=data.f_wheel_velocity_FL_ms
        pub_msg.f_wheel_velocity_FR_ms=data.f_wheel_velocity_FR_ms
        pub_msg.f_wheel_velocity_RL_ms=data.f_wheel_velocity_RL_ms
        pub_msg.f_wheel_velocity_RR_ms=data.f_wheel_velocity_RR_ms
        pub_msg.f_car_velocity_ms=data.f_car_velocity_ms
        pub_msg.i_throttle=data.i_throttle
        mbed_flag=1


        # 토크벡터링 ON
        if(data.c_torque_mode_flag==1):
            self.torque_on_off.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:80pt;\">ON</span></p></body></html>"))
            self.torque_on_off.setStyleSheet("\n"
"color: rgb(213, 0, 3);\n"
"font: 50pt \"배달의민족 한나체 Air\";\n"
" background-color: none;")
            self.ON_light.setStyleSheet("QFrame{\n"
"    background-color: rgba(255, 255, 51, 100);\n"
"\n"
"    border-radius: 60px;    \n"
"    \n"
"}")    


        # 토크벡터링 OFF
        else :
            self.torque_on_off.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:80pt;\">OFF</span></p></body></html>"))
            self.torque_on_off.setStyleSheet("\n"
"color: rgb(52,101,164);\n"
"font: 50pt \"배달의민족 한나체 Air\";\n"
" background-color: none;")
            self.ON_light.setStyleSheet("QFrame{\n"
"    background-color: rgba(178,190,197,100);\n"
"\n"
"    border-radius: 60px;    \n"
"    \n"
"}")



        # 현재 속도 출력
        self.velocity.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:100pt; font-weight:600;\">%dkm/h</span></p></body></html>" %int(data.f_car_velocity_ms)))


        # 토크 시각화 FL
        if (data.c_motor_mode_flag[0]==1) :
            rgb_torque=int(data.f_motor_torque_FL_Nm*RGB_CONST)

            if( rgb_torque < 136 ):
                rgb_torque = 79 + rgb_torque
                self.FL_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(215, %d, 79, 50);\n" 
"\n"
"    border-radius: 60px;    \n"
"    \n"
"}" %rgb_torque )
                self.FL_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(215, %d, 79, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

            elif ( rgb_torque < 136*2 ):
                rgb_torque = 215 - ( rgb_torque - 136 )
                self.FL_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(%d, 215, 79, 50);\n" 
"\n"
"    border-radius: 60px;    \n"
"    \n"
"}" %rgb_torque )
                self.FL_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(%d, 215, 79, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

            elif ( rgb_torque < 136*3 ):
                rgb_torque = 79 + ( rgb_torque - 136*2 )
                self.FL_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(79, 215, %d, 50);\n" 
"\n"
"    border-radius: 60px;    \n"
"    \n"
"}" %rgb_torque )
                self.FL_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(79, 215, %d, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

            elif ( rgb_torque < 136*4 ):
                rgb_torque = 215 - ( rgb_torque - 136*3 )
                self.FL_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(79, %d, 215, 50);\n" 
"\n"
"    border-radius: 60px;    \n"
"    \n"
"}" %rgb_torque )
                self.FL_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(79, %d, 215, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

        else :
            self.FL_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(0, 0, 0, 50);\n"
"\n"
"    border-radius: 60px;    \n"
"    \n"
"}")
            self.FL_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(0, 0, 0, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}")


        # 토크 시각화 FR
        if (data.c_motor_mode_flag[1]==1) :
            rgb_torque=int(data.f_motor_torque_FR_Nm*RGB_CONST)

            if( rgb_torque < 136 ):
                rgb_torque = 79 + rgb_torque
                self.FR_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(215, %d, 79, 50);\n" 
"\n"
"    border-radius: 60px;    \n"
"    \n"
"}" %rgb_torque )
                self.FR_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(215, %d, 79, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

            elif ( rgb_torque < 136*2 ):
                rgb_torque = 215 - ( rgb_torque - 136 )
                self.FR_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(%d, 215, 79, 50);\n" 
"\n"
"    border-radius: 60px;    \n"
"    \n"
"}" %rgb_torque )
                self.FR_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(%d, 215, 79, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

            elif ( rgb_torque < 136*3 ):
                rgb_torque = 79 + ( rgb_torque - 136*2 )
                self.FR_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(79, 215, %d, 50);\n" 
"\n"
"    border-radius: 60px;    \n"
"    \n"
"}" %rgb_torque )
                self.FR_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(79, 215, %d, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

            elif ( rgb_torque < 136*4 ):
                rgb_torque = 215 - ( rgb_torque - 136*3 )
                self.FR_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(79, %d, 215, 50);\n" 
"\n"
"    border-radius: 60px;    \n"
"    \n"
"}" %rgb_torque )
                self.FR_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(79, %d, 215, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

        else :
            self.FR_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(0, 0, 0, 50);\n"
"\n"
"    border-radius: 60px;    \n"
"    \n"
"}")
            self.FR_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(0, 0, 0, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}")

        # 토크 시각화 RL
        if (data.c_motor_mode_flag[0]==1) :
            rgb_torque=int(data.f_motor_torque_RL_Nm*RGB_CONST)

            if( rgb_torque < 136 ):
                rgb_torque = 79 + rgb_torque
                self.RL_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(215, %d, 79, 50);\n" 
"\n"
"    border-radius: 70px;    \n"
"    \n"
"}" %rgb_torque )
                self.RL_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(215, %d, 79, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

            elif ( rgb_torque < 136*2 ):
                rgb_torque = 215 - ( rgb_torque - 136 )
                self.RL_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(%d, 215, 79, 50);\n" 
"\n"
"    border-radius: 70px;    \n"
"    \n"
"}" %rgb_torque )
                self.RL_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(%d, 215, 79, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

            elif ( rgb_torque < 136*3 ):
                rgb_torque = 79 + ( rgb_torque - 136*2 )
                self.RL_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(79, 215, %d, 50);\n" 
"\n"
"    border-radius: 70px;    \n"
"    \n"
"}" %rgb_torque )
                self.RL_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(79, 215, %d, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

            elif ( rgb_torque < 136*4 ):
                rgb_torque = 215 - ( rgb_torque - 136*3 )
                self.RL_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(79, %d, 215, 50);\n" 
"\n"
"    border-radius: 70px;    \n"
"    \n"
"}" %rgb_torque )
                self.RL_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(79, %d, 215, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

        else :
            self.RL_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(0, 0, 0, 50);\n"
"\n"
"    border-radius: 70px;    \n"
"    \n"
"}")
            self.RL_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(0, 0, 0, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}")

        # 토크 시각화 RR
        if (data.c_motor_mode_flag[3]==1) :
            rgb_torque=int(data.f_motor_torque_RR_Nm*RGB_CONST)

            if( rgb_torque < 136 ):
                rgb_torque = 79 + rgb_torque
                self.RR_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(215, %d, 79, 50);\n" 
"\n"
"    border-radius: 70px;    \n"
"    \n"
"}" %rgb_torque )
                self.RR_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(215, %d, 79, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

            elif ( rgb_torque < 136*2 ):
                rgb_torque = 215 - ( rgb_torque - 136 )
                self.RR_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(%d, 215, 79, 50);\n" 
"\n"
"    border-radius: 70px;    \n"
"    \n"
"}" %rgb_torque )
                self.RR_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(%d, 215, 79, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

            elif ( rgb_torque < 136*3 ):
                rgb_torque = 79 + ( rgb_torque - 136*2 )
                self.RR_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(79, 215, %d, 50);\n" 
"\n"
"    border-radius: 70px;    \n"
"    \n"
"}" %rgb_torque )
                self.RR_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(79, 215, %d, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

            elif ( rgb_torque < 136*4 ):
                rgb_torque = 215 - ( rgb_torque - 136*3 )
                self.RR_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(79, %d, 215, 50);\n" 
"\n"
"    border-radius: 70px;    \n"
"    \n"
"}" %rgb_torque )
                self.RR_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(79, %d, 215, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}" %rgb_torque )

        else :
            self.RR_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(0, 0, 0, 50);\n"
"\n"
"    border-radius: 70px;    \n"
"    \n"
"}")
            self.RR_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(0, 0, 0, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}")


        # throttle 게이지
        self.PedalThrottle.setProperty("value", data.i_throttle)


    # GPS 통신 Slot 함수
    @pyqtSlot(NavSatFix)
    def SettingByGPS(self,data):
        _translate = QtCore.QCoreApplication.translate
        global START_POINT, START_WIDTH
        global pub, pub_msg
        global mbed_flag, GPS_flag
        latitude=data.latitude
        longitude=data.longitude
        #print('SettingByGPS')
        
        # flag check and publish
        if (mbed_flag==1 and GPS_flag==1):
            print('gps_pub')
            pub.publish(pub_msg)
            mbed_flag=0
            GPS_flag=0

        # 직사각형 start line을 구상하고 조건문 작성. (START_POINT 값이 직사각형의 중심)
        if (self.start_flag==0):
            if  (latitude<(START_POINT[0]+START_WIDTH[0]) and 
                 latitude>(START_POINT[0]-START_WIDTH[0]) and
                 longitude<(START_POINT[1]+START_WIDTH[1]) and
                 longitude>(START_POINT[1]-START_WIDTH[1])) :
                self.start_flag=1
                self.lap+=1
                self.start_time_ref=time.time()
                self.total_time_ref=self.start_time_ref

        elif (self.start_flag==1):
            if  (latitude<(START_POINT[0]+START_WIDTH[0]) and 
                 latitude>(START_POINT[0]-START_WIDTH[0]) and
                 longitude<(START_POINT[1]+START_WIDTH[1]) and
                 longitude>(START_POINT[1]-START_WIDTH[1])) :
                if (time.time()-self.start_time_ref>10) :
                    self.lap+=1
                    self.lap_time_ref=time.time()-self.start_time_ref
                    self.start_time_ref=time.time()
                    self.lap_time_prev=str(int(self.lap_time_ref//60)).zfill(2)+":"+str(int(self.lap_time_ref%60//1)).zfill(2)+":"+str(int(self.lap_time_ref%1*100)).zfill(2)

            self.start_duration=time.time()-self.start_time_ref
            self.total_duration=time.time()-self.total_time_ref
            self.lap_time_cur=str(int(self.start_duration//60)).zfill(2)+":"+str(int(self.start_duration%60//1)).zfill(2)+":"+str(int(self.start_duration%1*100)).zfill(2)
            self.total_time=str(int(self.total_duration//3600)).zfill(2)+":"+str(int(self.total_duration%3600//60)).zfill(2)+":"+str(int(self.total_duration%60)).zfill(2)
            
            # Setting publish msg 
            pub_msg.latitude=latitude
            pub_msg.longitude=longitude
            pub_msg.lap=self.lap
            pub_msg.lap_time_cur=self.lap_time_cur
            pub_msg.lap_time_prev=self.lap_time_prev
            pub_msg.total_time=self.total_time
            GPS_flag=1

            # 이전 랩타임 출력
            self.lap_timer_prev.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:62pt;\">%s</span></p></body></html>")%("/"+self.lap_time_prev))

            # 현재 랩타임 출력
            self.lap_timer_cur.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:84pt; font-weight:600;\">%s</span></p></body></html>" %self.lap_time_cur))

            # 총 주행시간 출력
            self.timer.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">%s</p></body></html>" %self.total_time))
        

        # lap 수 출력
        self.current_lap.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:120pt;\">%d</span></p></body></html>" %self.lap))
        
        
        # lap 수 시각화
        self.lap_percent=float(1.0-(self.lap/MAX_LAP))
        if (self.lap_percent==1.0) :
            self.lap_percent=0.997
        if (self.lap_percent==0.0) :
            self.lap_percent=0.003
        print(self.lap_percent)

        self.lappercentage.setStyleSheet("QFrame{\n"
"    border-radius: 200px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:%.3f rgba(255, 255, 255, 0), stop:%.3f rgba(255, 43, 82, 255));\n"
"} " %(self.lap_percent, self.lap_percent+0.001))



def main():
    global pub, pub_msg
    #QApllication: 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #rospy 초기화
    rospy.init_node('Main_System')
    #Subscriber 생성
    rospy.Subscriber('carstate',CarState,callbackByMbed,myWindow)
    rospy.Subscriber('ublox_gps/fix',NavSatFix,callbackByGPS,myWindow)

    #first Publish
    pub.publish(pub_msg)

    #통신 속도 결정
    rospy.Rate(8)

    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

    #ros 통신 반복
    rospy.spin()
                     
def callbackByMbed(data,window):
    window.emitSignalFromMbed(data)

def callbackByGPS(data,window):
    window.emitSiganlFromGPS(data)

if __name__ == "__main__" :
    main()
