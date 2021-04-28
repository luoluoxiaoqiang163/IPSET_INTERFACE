# 主窗口的导入
from leadcamera_4006s_ipset import Ui_MainWindow_LEADCAMERA4006s_IPSET

# pyqt5库的导入
from PyQt5.QtWidgets import QStyleFactory, QApplication, QMainWindow, QWidget, QLineEdit, QListView, QHBoxLayout, QGridLayout, QMessageBox, QFileDialog, QStatusBar, QToolTip
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QIODevice, pyqtSignal, QThread
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

# 其它工具库的使用
import sys
import os
import re  # 正则表达式的库
from psutil import net_if_addrs  # 网卡信息接口
import socket  # 网络库的导入
from interface_style.CommonHelper import CommonHelper  # 界面美化库的导入

class Main(QMainWindow, QWidget, Ui_MainWindow_LEADCAMERA4006s_IPSET):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化界面
        self.setWindowTitle("IP_Config")
        self.lead_icon = QIcon("./images/leadPic2.png")
        self.setWindowIcon(self.lead_icon)
        self.mxq_messsagebox = QMessageBox()  # 错误信息弹出栏
        self.ip2mac_show()  # 搜索本机的ip与mac并且列出
        self.listWidget_ip2mac_show.itemClicked.connect(self.ip2mac_set_show)  # 点击时连接设置ip2mac的设置显示函数
        self.pushButton_set_ip2mac.clicked.connect(self.arplist_bind)  # 绑定当前相机的ip与mac地址

        self.LoadStyle()  # 界面的美化函数

    def LoadStyle(self):
        """界面美化文件的载入"""
        styleFile = './interface_style/style.qss'
        qssStyle = CommonHelper.readQss(styleFile)
        self.setStyleSheet(qssStyle)
        # 分别给各个部件修饰
        self.listWidget_ip2mac_show.setStyleSheet("QWidget{color:white;background-color:rgb(46,49,66);}")

    def arplist_bind(self):
        """将相机的mac与ip地址绑定在静态列表上"""
        if (self.lineEdit_camera_ip.text() != '') and (self.lineEdit_camera_mac.text() != '') and (self.lineEdit_pc_ip.text() != '') and (self.lineEdit_pc_mac.text() != ''):
            pc_ip = self.lineEdit_pc_ip.text()
            pc_mac = self.lineEdit_pc_mac.text()
            camera_ip = self.lineEdit_camera_ip.text()
            camera_mac = self.lineEdit_camera_mac.text()
            print("mac与ip确认有值")
        else:
            self.mxq_messsagebox.warning(self, "arp绑定错误", "列表的ip与mac为空", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print("没有填入的ip或mac值")
            return

        with os.popen(r'arp -a') as f1:
            interface_ip2idx_list = []  # 网卡ip与识别码的序列
            line = f1.readline()
            interface_num = -1
            while line:
                print(line)
                if "接口:" in line:
                    interface_num += 1
                    str_flag1 = re.search("接口:", line).span()
                    str_flag2 = re.search("---", line).span()
                    interface_ip = line[str_flag1[1]:str_flag2[0]].strip()  # 字符串取出ip地址，去掉首尾的空格
                    interface_idx = line[str_flag2[1]:].strip()  # ip的识别号idx
                    interface_ip2idx_list.append([interface_ip, str(int(interface_idx, 16))])
                else:
                    if "静态" in line or "动态" in line:
                        ip2mac = line.split()
                        interface_ip2idx_list[interface_num].append(ip2mac)
                line = f1.readline()
        print(interface_ip2idx_list)

        # 找到目标网卡并确认是否被分配
        idx = None
        for i in interface_ip2idx_list:
            if i[0] == pc_ip:
                idx = i[1]
                for j in i[2:]:
                    if camera_ip == j[0]:
                        #remove_ip_ret = input("已有ip" + j[0] + " " + j[1] + " " + j[2] + " 是否删除(Y/N)")
                        arp_ip_mac_text_warning = "该ip缓存列表已有ip:mac "+ j[0]+":"+j[1]+":"+ j[2] + "，是否删除"
                        remove_ip_ret = self.mxq_messsagebox.warning(self, "arp绑定错误", arp_ip_mac_text_warning, QMessageBox.Yes | QMessageBox.No,
                                                                     QMessageBox.Yes)
                        if remove_ip_ret == QMessageBox.No:
                            return
                        comand = 'netsh -c "i i" delete neighbors ' + idx +" " + j[0] + " " + j[1]
                        with os.popen(comand) as f1:
                            ret = f1.read()
                        print(ret)
                break
        
        if idx == None:
            self.mxq_messsagebox.warning(self, "arp绑定错误", "该ip没有arp缓存列表或没有网卡具有该ip", QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            return

        comand = 'netsh -c "i i" add neighbors ' + idx + ' ' + camera_ip + ' ' + camera_mac
        with os.popen(comand) as f1:
            ret = f1.read()
        if ret != "\n":
            self.mxq_messsagebox.warning(self, "arp绑定结果", ret, QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            return
        self.mxq_messsagebox.warning(self, "arp绑定结果", "绑定成功", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        self.IPSET_G6500(pc_ip, pc_mac, camera_ip, camera_mac)

    def IPSET_G6500(self, pc_ip, pc_mac, camera_ip, camera_mac):
        """6500M相机设置内部ip"""
        camera_addr = (camera_ip, 8800)
        pc_addr = (pc_ip, 9000)
        pc_ip_data = re.search('(\d+).(\d+).(\d+).(\d+)', pc_ip)
        pc_mac_data = re.search('([0-9a-fA-F]+)-([0-9a-fA-F]+)-([0-9a-fA-F]+)-([0-9a-fA-F]+([0-9a-fA-F]+)-([0-9a-fA-F]+))', pc_mac)
        data_pc_ip = self.IPSET_G6500_DATA(63, int(pc_ip_data.group(1)), int(pc_ip_data.group(2)), int(pc_ip_data.group(3)), int(pc_ip_data.group(4)))
        data_pc_mac1 = self.IPSET_G6500_DATA(61, 0, 0, int(pc_mac_data.group(1)), int(pc_mac_data.group(2)))
        data_pc_mac2 = self.IPSET_G6500_DATA(62, int(pc_mac_data.group(3)), int(pc_mac_data.group(4)), int(pc_mac_data.group(5)), int(pc_mac_data.group(6)))
        self.camera_sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.camera_sk.bind(pc_addr)
        self.camera_sk.sendto(data_pc_mac1, camera_addr)
        self.camera_sk.sendto(data_pc_mac2, camera_addr)
        print("dst_mac done")
        self.camera_sk.sendto(data_pc_ip, camera_addr)
        print("dst_ip done")




    def IPSET_G6500_DATA(commandinput, dataI1, dataI2, dataI3, dataI4):

        commandinput = commandinput * 4
        # RorWinput = input("请选择读或者写(读完为1，写为0):")
        comaddr1 = 0x00  # 命令地址1
        comaddr2 = 0x00  # 命令地址2
        comaddr3 = 0x00  # 命令地址3
        comaddr4 = 0x00  # 命令地址4
        datalenth1 = 0x00  # 数据长度1
        datalenth2 = 0x04  # 数据长度2
        Rev = 0x00  # 保留字节

        com1 = ((commandinput >> 8) & 0xff) | 0x00  # 写指令
        com2 = commandinput & 0xff
        # datainput = input("请输入数据")

        data1 = dataI1 & 0xff
        data2 = dataI2 & 0xff
        data3 = dataI3 & 0xff
        data4 = dataI4 & 0xff

        checksum = (0x00 + com1 + com2 + comaddr1 + comaddr2 + \
                    comaddr3 + comaddr4 + datalenth1 + datalenth2 + \
                    Rev + data1 + data2 + data3 + data4) & 0xff  # 校验和暂时不加
        command = [0xaa, 0x54, 0x00, com1, com2, comaddr1, comaddr2, comaddr3, comaddr4, \
                   datalenth1, datalenth2, Rev, data1, data2, data3, data4, checksum, 0xaa, 0x5c]

        return command

    def IPSET_4006A(self, pc_ip, pc_mac, camera_ip, camera_mac):
        """4006A相机的内部ip"""

    def ip2mac_set_show(self, item):
        """将选中的ip与mac填入选择项中"""
        str_flag_ip = re.search(":", item.text()).span()
        # print(str_flag_ip)
        pc_ip_text = item.text()[:str_flag_ip[0]].strip()
        pc_mac_text = item.text()[str_flag_ip[1]:].strip()
        self.lineEdit_pc_ip.setText(pc_ip_text)
        self.lineEdit_pc_mac.setText(pc_mac_text)





    def ip2mac_show(self):
        """搜索ip与mac的对应关系并且列出"""
        ip2maclist = []
        for k, v in net_if_addrs().items():
            if len(v) >= 2:
                ip_address = v[1][1]
                mac_address = v[0][1]
                if '-' in mac_address and len(mac_address) == 17:
                    ip2maclist.append([ip_address, mac_address])
        # 添加ip与mac地址的对应关系
        for ip2macname in ip2maclist:
            self.listWidget_ip2mac_show.addItem(ip2macname[0]+" : "+ip2macname[1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec())




