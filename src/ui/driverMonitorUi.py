# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitorUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1920, 1080)
        Dialog.setStyleSheet("\n"
"background-color: rgb(229, 230, 229);\n"
"\n"
"")
        self.circularBg = QtWidgets.QFrame(Dialog)
        self.circularBg.setGeometry(QtCore.QRect(1370, 220, 400, 400))
        self.circularBg.setStyleSheet("QFrame{\n"
"    border-radius: 200px;    \n"
"    background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg.setObjectName("circularBg")
        self.lappercentage = QtWidgets.QFrame(self.circularBg)
        self.lappercentage.setGeometry(QtCore.QRect(0, 0, 400, 400))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(30)
        self.lappercentage.setFont(font)
        self.lappercentage.setStyleSheet("QFrame{\n"
"    border-radius: 200px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90,  stop:0.75 rgba(255, 255, 255, 0),stop:0.752 rgba(255, 43, 82, 255));\n"
"} ")
        self.lappercentage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lappercentage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lappercentage.setObjectName("lappercentage")
        self.circularContainer_3 = QtWidgets.QFrame(self.lappercentage)
        self.circularContainer_3.setGeometry(QtCore.QRect(20, 20, 360, 360))
        self.circularContainer_3.setBaseSize(QtCore.QSize(0, 0))
        self.circularContainer_3.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"    border-radius: 180px;    \n"
"    \n"
"}")
        self.circularContainer_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularContainer_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularContainer_3.setObjectName("circularContainer_3")
        self.current_lap = QtWidgets.QLabel(self.circularContainer_3)
        self.current_lap.setGeometry(QtCore.QRect(110, 70, 131, 171))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.current_lap.setFont(font)
        self.current_lap.setStyleSheet(" padding: 0px; background-color: none;\n"
"font: 72pt \"Agency FB\";\n"
"color: rgb(2, 73, 103);")
        self.current_lap.setAlignment(QtCore.Qt.AlignCenter)
        self.current_lap.setIndent(-1)
        self.current_lap.setObjectName("current_lap")
        self.laps = QtWidgets.QLabel(self.circularContainer_3)
        self.laps.setGeometry(QtCore.QRect(130, 240, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.laps.setFont(font)
        self.laps.setStyleSheet("color: rgb(148, 148, 216); background-color: none;")
        self.laps.setAlignment(QtCore.Qt.AlignCenter)
        self.laps.setObjectName("laps")
        self.FL_state = QtWidgets.QFrame(Dialog)
        self.FL_state.setGeometry(QtCore.QRect(800, 280, 120, 120))
        self.FL_state.setBaseSize(QtCore.QSize(0, 0))
        self.FL_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(255, 0, 4, 50);\n"
"\n"
"    border-radius: 60px;    \n"
"    \n"
"}")
        self.FL_state.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FL_state.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FL_state.setObjectName("FL_state")
        self.FL_state_2 = QtWidgets.QFrame(self.FL_state)
        self.FL_state_2.setGeometry(QtCore.QRect(40, 20, 51, 81))
        self.FL_state_2.setBaseSize(QtCore.QSize(0, 0))
        self.FL_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(255, 0, 4, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}")
        self.FL_state_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FL_state_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FL_state_2.setObjectName("FL_state_2")
        self.RL_state = QtWidgets.QFrame(Dialog)
        self.RL_state.setGeometry(QtCore.QRect(790, 530, 140, 140))
        self.RL_state.setBaseSize(QtCore.QSize(0, 0))
        self.RL_state.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(125, 255, 216,200);\n"
"\n"
"    border-radius: 70px;    \n"
"    \n"
"}")
        self.RL_state.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RL_state.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RL_state.setObjectName("RL_state")
        self.RL_state_2 = QtWidgets.QFrame(self.RL_state)
        self.RL_state_2.setGeometry(QtCore.QRect(40, 20, 71, 91))
        self.RL_state_2.setBaseSize(QtCore.QSize(0, 0))
        self.RL_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(125, 255, 216,200);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}")
        self.RL_state_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RL_state_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RL_state_2.setObjectName("RL_state_2")
        self.RR_state = QtWidgets.QFrame(Dialog)
        self.RR_state.setGeometry(QtCore.QRect(1020, 530, 140, 140))
        self.RR_state.setBaseSize(QtCore.QSize(0, 0))
        self.RR_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(255, 0, 4, 50);\n"
"\n"
"    border-radius: 70px;    \n"
"    \n"
"}")
        self.RR_state.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RR_state.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RR_state.setObjectName("RR_state")
        self.RR_state_2 = QtWidgets.QFrame(self.RR_state)
        self.RR_state_2.setGeometry(QtCore.QRect(30, 30, 71, 81))
        self.RR_state_2.setBaseSize(QtCore.QSize(0, 0))
        self.RR_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(255, 0, 4, 50);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}")
        self.RR_state_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RR_state_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RR_state_2.setObjectName("RR_state_2")
        self.torquevectoring = QtWidgets.QLabel(Dialog)
        self.torquevectoring.setGeometry(QtCore.QRect(570, 30, 631, 121))
        self.torquevectoring.setStyleSheet("\n"
"font: 32pt \"배달의민족 한나체 Air\";\n"
" background-color: none;")
        self.torquevectoring.setObjectName("torquevectoring")
        self.torque_on_off = QtWidgets.QLabel(Dialog)
        self.torque_on_off.setGeometry(QtCore.QRect(1140, 40, 181, 101))
        self.torque_on_off.setStyleSheet("color: rgb(52, 101, 164);\n"
"\n"
"font: 50pt \"배달의민족 한나체 Air\";\n"
" background-color: none;")
        self.torque_on_off.setObjectName("torque_on_off")
        self.torquevectoringbackground = QtWidgets.QLabel(Dialog)
        self.torquevectoringbackground.setGeometry(QtCore.QRect(570, 20, 801, 141))
        self.torquevectoringbackground.setStyleSheet("background-color: rgb(231, 221, 221);\n"
"\n"
"border-radius: 30px;    \n"
"")
        self.torquevectoringbackground.setText("")
        self.torquevectoringbackground.setObjectName("torquevectoringbackground")
        self.PedalThrottle = QtWidgets.QProgressBar(Dialog)
        self.PedalThrottle.setGeometry(QtCore.QRect(190, 200, 321, 771))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(32)
        self.PedalThrottle.setFont(font)
        self.PedalThrottle.setMouseTracking(False)
        self.PedalThrottle.setStyleSheet("QProgressBar\n"
"                    {\n"
"                    \n"
"    \n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(195, 221, 220);\n"
"    border-radius: 10px;\n"
"                    }\n"
"QProgressBar::chunk\n"
"                  {\n"
"                    \n"
"                    border-radius: 10px;\n"
"                    border-top-width: 10px;\n"
"                    border-right-width: 5px;\n"
"                    border-left-width: 5px;\n"
"                    border-style:solid;\n"
"                    margin:1px;\n"
"                    \n"
"    border-top-color: rgb(24, 112, 255);\n"
"    border-left-color: rgb(24, 112, 255);\n"
"    border-right-color: rgb(24, 112, 255);\n"
"     \n"
"    border-bottom-color: rgb(169, 217, 217);\n"
"\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(255, 114, 0);\n"
"                  }\n"
"")
        self.PedalThrottle.setProperty("value", 80)
        self.PedalThrottle.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.PedalThrottle.setTextVisible(False)
        self.PedalThrottle.setOrientation(QtCore.Qt.Vertical)
        self.PedalThrottle.setInvertedAppearance(False)
        self.PedalThrottle.setObjectName("PedalThrottle")
        self.throttle_0 = QtWidgets.QLabel(Dialog)
        self.throttle_0.setGeometry(QtCore.QRect(190, 950, 71, 10))
        self.throttle_0.setStyleSheet("background-color: rgb(254, 249, 255);\n"
"border-radius: 3px;")
        self.throttle_0.setText("")
        self.throttle_0.setObjectName("throttle_0")
        self.throttle_30 = QtWidgets.QLabel(Dialog)
        self.throttle_30.setGeometry(QtCore.QRect(190, 740, 321, 10))
        self.throttle_30.setStyleSheet("background-color: rgb(254, 249, 255);\n"
"border-radius: 3px;")
        self.throttle_30.setText("")
        self.throttle_30.setObjectName("throttle_30")
        self.throttle_60 = QtWidgets.QLabel(Dialog)
        self.throttle_60.setGeometry(QtCore.QRect(190, 520, 71, 10))
        self.throttle_60.setStyleSheet("background-color: rgb(254, 249, 255);\n"
"border-radius: 3px;")
        self.throttle_60.setText("")
        self.throttle_60.setObjectName("throttle_60")
        self.throttle_90 = QtWidgets.QLabel(Dialog)
        self.throttle_90.setGeometry(QtCore.QRect(190, 280, 321, 10))
        self.throttle_90.setStyleSheet("background-color: rgb(254, 249, 255);\n"
"border-radius: 3px;")
        self.throttle_90.setText("")
        self.throttle_90.setObjectName("throttle_90")
        self.throttle_100 = QtWidgets.QLabel(Dialog)
        self.throttle_100.setGeometry(QtCore.QRect(190, 200, 71, 10))
        self.throttle_100.setStyleSheet("background-color: rgb(254, 249, 255);\n"
"border-radius: 3px;\n"
"")
        self.throttle_100.setText("")
        self.throttle_100.setObjectName("throttle_100")
        self.throttle_80 = QtWidgets.QLabel(Dialog)
        self.throttle_80.setGeometry(QtCore.QRect(190, 360, 71, 10))
        self.throttle_80.setStyleSheet("background-color: rgb(254, 249, 255);\n"
"border-radius: 3px;")
        self.throttle_80.setText("")
        self.throttle_80.setObjectName("throttle_80")
        self.throttle_70 = QtWidgets.QLabel(Dialog)
        self.throttle_70.setGeometry(QtCore.QRect(190, 440, 321, 10))
        self.throttle_70.setStyleSheet("background-color: rgb(254, 249, 255);\n"
"border-radius: 3px;")
        self.throttle_70.setText("")
        self.throttle_70.setObjectName("throttle_70")
        self.throttle_50 = QtWidgets.QLabel(Dialog)
        self.throttle_50.setGeometry(QtCore.QRect(190, 600, 321, 10))
        self.throttle_50.setStyleSheet("background-color: rgb(254, 249, 255);\n"
"border-radius: 3px;")
        self.throttle_50.setText("")
        self.throttle_50.setObjectName("throttle_50")
        self.throttle_40 = QtWidgets.QLabel(Dialog)
        self.throttle_40.setGeometry(QtCore.QRect(190, 670, 71, 10))
        self.throttle_40.setStyleSheet("background-color: rgb(254, 249, 255);\n"
"border-radius: 3px;")
        self.throttle_40.setText("")
        self.throttle_40.setObjectName("throttle_40")
        self.throttle_20 = QtWidgets.QLabel(Dialog)
        self.throttle_20.setGeometry(QtCore.QRect(190, 820, 71, 10))
        self.throttle_20.setStyleSheet("background-color: rgb(254, 249, 255);\n"
"border-radius: 3px;")
        self.throttle_20.setText("")
        self.throttle_20.setObjectName("throttle_20")
        self.throttle_10 = QtWidgets.QLabel(Dialog)
        self.throttle_10.setGeometry(QtCore.QRect(190, 900, 321, 10))
        self.throttle_10.setStyleSheet("background-color: rgb(254, 249, 255);\n"
"border-radius: 3px;")
        self.throttle_10.setText("")
        self.throttle_10.setObjectName("throttle_10")
        self.velocity = QtWidgets.QLabel(Dialog)
        self.velocity.setGeometry(QtCore.QRect(690, 750, 581, 151))
        font = QtGui.QFont()
        font.setFamily("배달의민족 도현")
        font.setPointSize(100)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.velocity.setFont(font)
        self.velocity.setStyleSheet("font: 100pt \"배달의민족 도현\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.velocity.setObjectName("velocity")
        self.throttle_1 = QtWidgets.QLabel(Dialog)
        self.throttle_1.setGeometry(QtCore.QRect(140, 940, 41, 41))
        self.throttle_1.setStyleSheet("background-color: none;\n"
"font: 30pt \"배달의민족 도현\";\n"
"")
        self.throttle_1.setObjectName("throttle_1")
        self.throttle_21 = QtWidgets.QLabel(Dialog)
        self.throttle_21.setGeometry(QtCore.QRect(120, 810, 61, 41))
        self.throttle_21.setStyleSheet("background-color: none;\n"
"font: 30pt \"배달의민족 도현\";\n"
"")
        self.throttle_21.setObjectName("throttle_21")
        self.throttle_41 = QtWidgets.QLabel(Dialog)
        self.throttle_41.setGeometry(QtCore.QRect(120, 660, 61, 41))
        self.throttle_41.setStyleSheet("background-color: none;\n"
"font: 30pt \"배달의민족 도현\";\n"
"")
        self.throttle_41.setObjectName("throttle_41")
        self.throttle_61 = QtWidgets.QLabel(Dialog)
        self.throttle_61.setGeometry(QtCore.QRect(120, 510, 61, 41))
        self.throttle_61.setStyleSheet("background-color: none;\n"
"font: 30pt \"배달의민족 도현\";\n"
"")
        self.throttle_61.setObjectName("throttle_61")
        self.throttle_81 = QtWidgets.QLabel(Dialog)
        self.throttle_81.setGeometry(QtCore.QRect(120, 350, 61, 41))
        self.throttle_81.setStyleSheet("background-color: none;\n"
"font: 30pt \"배달의민족 도현\";\n"
"")
        self.throttle_81.setObjectName("throttle_81")
        self.throttle_101 = QtWidgets.QLabel(Dialog)
        self.throttle_101.setGeometry(QtCore.QRect(110, 190, 71, 41))
        font = QtGui.QFont()
        font.setFamily("배달의민족 도현")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.throttle_101.setFont(font)
        self.throttle_101.setStyleSheet("background-color: none;\n"
"font: 30pt \"배달의민족 도현\";\n"
"")
        self.throttle_101.setObjectName("throttle_101")
        self.ON_light = QtWidgets.QFrame(Dialog)
        self.ON_light.setGeometry(QtCore.QRect(1130, 20, 201, 141))
        self.ON_light.setBaseSize(QtCore.QSize(0, 0))
        self.ON_light.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(178, 190, 197, 100);\n"
"\n"
"    border-radius: 60px;    \n"
"    \n"
"}")
        self.ON_light.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ON_light.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ON_light.setObjectName("ON_light")
        self.FR_state = QtWidgets.QFrame(Dialog)
        self.FR_state.setGeometry(QtCore.QRect(1030, 280, 120, 120))
        self.FR_state.setBaseSize(QtCore.QSize(0, 0))
        self.FR_state.setStyleSheet("QFrame{\n"
"    background-color: rgba(255, 255, 51, 190);\n"
"\n"
"    border-radius: 60px;    \n"
"    \n"
"}")
        self.FR_state.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FR_state.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FR_state.setObjectName("FR_state")
        self.FR_state_2 = QtWidgets.QFrame(self.FR_state)
        self.FR_state_2.setGeometry(QtCore.QRect(30, 20, 44, 81))
        self.FR_state_2.setBaseSize(QtCore.QSize(0, 0))
        self.FR_state_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(255, 255, 51, 190);\n"
"\n"
"    border-radius: 15px;    \n"
"    \n"
"}")
        self.FR_state_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FR_state_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FR_state_2.setObjectName("FR_state_2")
        self.lap_timer_cur = QtWidgets.QLabel(Dialog)
        self.lap_timer_cur.setGeometry(QtCore.QRect(1330, 620, 491, 131))
        self.lap_timer_cur.setStyleSheet("font: 87 50pt \"Segoe UI Black\";")
        self.lap_timer_cur.setObjectName("lap_timer_cur")
        self.lap_timer_prev = QtWidgets.QLabel(Dialog)
        self.lap_timer_prev.setGeometry(QtCore.QRect(1380, 780, 391, 91))
        font = QtGui.QFont()
        font.setFamily("Gulim")
        font.setPointSize(25)
        self.lap_timer_prev.setFont(font)
        self.lap_timer_prev.setStyleSheet("background-color:none;\n"
"")
        self.lap_timer_prev.setObjectName("lap_timer_prev")
        self.timer = QtWidgets.QLabel(Dialog)
        self.timer.setGeometry(QtCore.QRect(1360, 880, 421, 85))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(70)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.timer.setFont(font)
        self.timer.setStyleSheet("font: 57 70pt \"Yu Gothic Medium\";\n"
"background-color:none;\n"
"")
        self.timer.setObjectName("timer")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(740, 230, 471, 471))
        self.label.setStyleSheet("image: url(:/car_top.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.lap_timer_cur.raise_()
        self.lap_timer_prev.raise_()
        self.timer.raise_()
        self.torquevectoringbackground.raise_()
        self.circularBg.raise_()
        self.torquevectoring.raise_()
        self.torque_on_off.raise_()
        self.PedalThrottle.raise_()
        self.throttle_0.raise_()
        self.throttle_30.raise_()
        self.throttle_60.raise_()
        self.throttle_90.raise_()
        self.throttle_100.raise_()
        self.throttle_80.raise_()
        self.throttle_70.raise_()
        self.throttle_50.raise_()
        self.throttle_40.raise_()
        self.throttle_20.raise_()
        self.throttle_10.raise_()
        self.velocity.raise_()
        self.throttle_1.raise_()
        self.throttle_21.raise_()
        self.throttle_41.raise_()
        self.throttle_61.raise_()
        self.throttle_81.raise_()
        self.throttle_101.raise_()
        self.ON_light.raise_()
        self.FL_state.raise_()
        self.FR_state.raise_()
        self.RL_state.raise_()
        self.RR_state.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.current_lap.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:120pt;\">4</span></p></body></html>"))
        self.laps.setText(_translate("Dialog", "<html><head/><body><p>laps</p></body></html>"))
        self.torquevectoring.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:90pt;\">토크벡터링 </span></p></body></html>"))
        self.torque_on_off.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:80pt;\">OFF</span></p></body></html>"))
        self.velocity.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:100pt; font-weight:600;\">00km/h</span></p></body></html>"))
        self.throttle_1.setText(_translate("Dialog", "0"))
        self.throttle_21.setText(_translate("Dialog", "20"))
        self.throttle_41.setText(_translate("Dialog", "40"))
        self.throttle_61.setText(_translate("Dialog", "60"))
        self.throttle_81.setText(_translate("Dialog", "80"))
        self.throttle_101.setText(_translate("Dialog", "100"))
        self.lap_timer_cur.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:84pt; font-weight:600;\">00:00:00</span></p></body></html>"))
        self.lap_timer_prev.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:62pt;\">/00:00:00</span></p></body></html>"))
        self.timer.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">00:00:00</p></body></html>"))
import hybridimages_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
