먼저 이 패키지 (custom_msg2_pkg_modified)를 ~/catkin_ws/src에 옮긴다.

실행 방법
0. catkin_make로 패키지 업데이트하기
	1) cd ~/catkin_ws
	2) catkin_make
	
1. python 파일 실행가능한 파일로 권한 변경
	1) cd ~/catkin_ws/src/custom_msg2_pkg/src
	2) ls 
	-> python 파일이 실행가능한 파일인지 확인. (초록색 글씨 = 실행가능한 파일임.)
	-> 실행가능한 파일이 아니라면 3. 실행 (흰색 글씨 = 실행불가능한 파일.)
	3) sudo chmod +x [파이썬파일명.py] (ex: sudo chmod +x CTui_proto2_modified.py)
	
2. roscore 
3. rosrun custom_msg2_pkg data_node_script.py
4. cd ~/catkin_ws/src/custom_msg2_pkg/src
5. rosrun custom_msg2_pkg CTui_proto2_modified.py
