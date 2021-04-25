# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'leadcamera_4006s_ipset.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_LEADCAMERA4006s_IPSET(object):
    def setupUi(self, MainWindow_LEADCAMERA4006s_IPSET):
        MainWindow_LEADCAMERA4006s_IPSET.setObjectName("MainWindow_LEADCAMERA4006s_IPSET")
        MainWindow_LEADCAMERA4006s_IPSET.resize(578, 394)
        self.centralwidget = QtWidgets.QWidget(MainWindow_LEADCAMERA4006s_IPSET)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_camera_mac = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_camera_mac.setObjectName("lineEdit_camera_mac")
        self.gridLayout.addWidget(self.lineEdit_camera_mac, 3, 1, 1, 1)
        self.lineEdit_camera_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_camera_ip.setObjectName("lineEdit_camera_ip")
        self.gridLayout.addWidget(self.lineEdit_camera_ip, 2, 1, 1, 1)
        self.label_pc_mac = QtWidgets.QLabel(self.centralwidget)
        self.label_pc_mac.setObjectName("label_pc_mac")
        self.gridLayout.addWidget(self.label_pc_mac, 1, 0, 1, 1)
        self.lineEdit_pc_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pc_ip.setObjectName("lineEdit_pc_ip")
        self.gridLayout.addWidget(self.lineEdit_pc_ip, 0, 1, 1, 1)
        self.label_camera_ip = QtWidgets.QLabel(self.centralwidget)
        self.label_camera_ip.setObjectName("label_camera_ip")
        self.gridLayout.addWidget(self.label_camera_ip, 2, 0, 1, 1)
        self.label_pc_ip = QtWidgets.QLabel(self.centralwidget)
        self.label_pc_ip.setObjectName("label_pc_ip")
        self.gridLayout.addWidget(self.label_pc_ip, 0, 0, 1, 1)
        self.lineEdit_pc_mac = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pc_mac.setObjectName("lineEdit_pc_mac")
        self.gridLayout.addWidget(self.lineEdit_pc_mac, 1, 1, 1, 1)
        self.label_camera_mac = QtWidgets.QLabel(self.centralwidget)
        self.label_camera_mac.setObjectName("label_camera_mac")
        self.gridLayout.addWidget(self.label_camera_mac, 3, 0, 1, 1)
        self.listWidget_ip2mac_show = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_ip2mac_show.setObjectName("listWidget_ip2mac_show")
        self.gridLayout.addWidget(self.listWidget_ip2mac_show, 0, 2, 4, 1)
        self.label_message_show = QtWidgets.QLabel(self.centralwidget)
        self.label_message_show.setObjectName("label_message_show")
        self.gridLayout.addWidget(self.label_message_show, 7, 0, 1, 3)
        self.pushButton_set_ip2mac = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_set_ip2mac.setObjectName("pushButton_set_ip2mac")
        self.gridLayout.addWidget(self.pushButton_set_ip2mac, 4, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 5)
        MainWindow_LEADCAMERA4006s_IPSET.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_LEADCAMERA4006s_IPSET)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 26))
        self.menubar.setObjectName("menubar")
        MainWindow_LEADCAMERA4006s_IPSET.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_LEADCAMERA4006s_IPSET)
        self.statusbar.setObjectName("statusbar")
        MainWindow_LEADCAMERA4006s_IPSET.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_LEADCAMERA4006s_IPSET)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_LEADCAMERA4006s_IPSET)

    def retranslateUi(self, MainWindow_LEADCAMERA4006s_IPSET):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_LEADCAMERA4006s_IPSET.setWindowTitle(_translate("MainWindow_LEADCAMERA4006s_IPSET", "MainWindow"))
        self.label_pc_mac.setText(_translate("MainWindow_LEADCAMERA4006s_IPSET", "本地mac"))
        self.label_camera_ip.setText(_translate("MainWindow_LEADCAMERA4006s_IPSET", "相机IP"))
        self.label_pc_ip.setText(_translate("MainWindow_LEADCAMERA4006s_IPSET", "本地Ip"))
        self.label_camera_mac.setText(_translate("MainWindow_LEADCAMERA4006s_IPSET", "相机mac"))
        self.label_message_show.setText(_translate("MainWindow_LEADCAMERA4006s_IPSET", "配置信息"))
        self.pushButton_set_ip2mac.setText(_translate("MainWindow_LEADCAMERA4006s_IPSET", "设置"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_LEADCAMERA4006s_IPSET = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_LEADCAMERA4006s_IPSET()
    ui.setupUi(MainWindow_LEADCAMERA4006s_IPSET)
    MainWindow_LEADCAMERA4006s_IPSET.show()
    sys.exit(app.exec_())
