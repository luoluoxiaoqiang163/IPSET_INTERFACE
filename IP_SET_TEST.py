# 自研相机IP设置
import os
import re

# 输入想要寻找mac地址的本机ip
# pc_ip = input("输入本机ip:")
# camera_ip = input("输入相机ip地址:")
# camera_mac = input("输入相机mac地址:")
pc_ip = "192.168.8.6"
camera_ip = "192.168.8.15"
camera_mac = "f1-f2-f3-f4-f5-f8"
command_arplist_query = r'arp -a -N ' + pc_ip
command_arplist_query
# 返回命令的返回

with os.popen( r'arp -a') as f1:
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
        for j in i[1:]:
            if camera_ip == j[0]:
                remove_ip_ret = input("已有ip" + j[0] + " " + j[1] + " " + j[2] + " 是否删除(Y/N)")
                if remove_ip_ret == "Y":
                    comand = 'netsh -c "i i" delete neighbors ' + idx
                    with os.popen(comand) as f1:
                        ret = f1.read()
                    print(ret)
        break
if idx == None:
    print("该ip没有arp缓存列表或没有网卡具有ip:"+ pc_ip)

comand = 'netsh -c "i i" add neighbors ' + idx + ' ' + camera_ip + ' ' + camera_mac
with os.popen(comand) as f1:
    ret = f1.read()
    print(ret)

"""
with os.popen(r'ipconfig') as f2:
	text = f2.read()
print(text)
"""

