from psutil import net_if_addrs
ip2maclist = []
for k, v in net_if_addrs().items():
    if len(v) >= 2:
        ip_address = v[1][1]
        mac_address = v[0][1]
        if '-' in mac_address and len(mac_address) == 17:
            ip2maclist.append([ip_address, mac_address])
print(ip2maclist)




