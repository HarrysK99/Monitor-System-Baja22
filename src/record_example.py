#!/usr/bin/env python3

import rospy
import time
import sys
from sensor_msgs.msg import NavSatFix

global latitude, longitude 
global comm_time
global start_time, lap 

comm_time=time.time()
latitude=0 
longitude=0
lap=0
start_time=time.time()

# File IO variables
global fd
fd = None
global fileWriteLineCount
fileWriteLineCount = 0


def file_writeLine(_str):
    global fd
    global fileWriteLineCount
    if(fd == None): # 맨 처음 파일 여는 것.
        fd = open("./test1.txt", 'w') # .은 현재디렉토리 위치. 바꾸고 싶으면 절대위치 가능.
    fd.write(_str+"\n")
    
    fileWriteLineCount += 1
    if(fileWriteLineCount == 10 and not fd.closed):
        fd.close()
        fileNameCount = int(fd.name.split(".")[1][-1:]) # split 하면 0번째 : 빈 문자열 | 1번째 : /test1 | 2번째 : txt => 1번째 원소에서 뒤에서 첫 번째 문자부터 끝까지 출력
        fd = open("." + fd.name.split(".")[1][:5] + str(fileNameCount + 1) +".txt", "w")
        
    
        


        

def callback_spin(msg):
    print(msg)
    global latitude, longitude, start_time, lap, comm_time
    duration=time.time()-start_time

    latitude=msg.latitude
    longitude=msg.longitude

    print("============================")
    print("lap : " + str(lap))
    print("latitude : " + str(latitude))
    print("longitude : " + str(longitude))

    if latitude>37.5418:
        if longitude>127.079129:
            if duration>10 :
                lap+=1            # +1 lap
                start_time=time.time() # timer reset
            
   # if latitude<37.541900 and latitude>37.541350 :
   #     if longitude<127.08000 and longitude>127.07900:
   #         print("timer : "+ str(duration))

    print("timer : "+str(duration))
    print("============================")

    file_writeLine(str(lap) + " " + str(latitude) + " " + str(longitude) + " " + str(duration))

def callback_shutdown():
    if(fd != None and not fd.closed):
        fd.close()
        
    
def main():
    rospy.init_node('receiver_serial',anonymous=False)
    sub=rospy.Subscriber('ublox_gps/fix',NavSatFix,callback_spin)
    # spin 종료 될 때 callback 실행
    rospy.on_shutdown(callback_shutdown)
    print(1)
    rospy.spin()
    


if __name__ == "__main__" :
    main()
