#!/usr/bin/python
# --*-- coding:utf-8 --*--

import wmi
import random
import sys
import os

print('--------------------------------------------------------')
print('脚本网段为192.168.1.X, 解决公司IP冲突')
print('选择自己的需要修改的网卡')
print('--------------------------------------------------------')


def changip():
    wmiService = wmi.WMI()
    colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    if len(colNicConfigs) < 1:
        print('没有找到可用的网络适配器')
    print('\n')
    print('----------------------------------')
    for i in range(len(colNicConfigs)):
        print(str(i) + ":", "IP:", colNicConfigs[i].IPAddress, "Name:", colNicConfigs[i].Description)
    print("----------------------------------")
    i = input('选择以太网卡:\n')
    objNicConfig = colNicConfigs[int(i)]
    ip_last = random.randint(1, 254)
    arrIPAddresses = ['192.168.1' + '.' + str(ip_last)]
    arrSubnetMasks = ['255.255.255.0']
    arrDefaultGateways = ['192.168.1.1']
    arrGatewayCostMetrics = [1]
    arrDNSServers = ['8.8.8.8', '8.8.4.4']
    objNicConfig.SetGateways(DefaultIPGateway=arrDefaultGateways, GatewayCostMetric=arrGatewayCostMetrics)
    objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder=arrDNSServers)
    returnValue=objNicConfig.EnableStatic(IPAddress=arrIPAddresses, SubnetMask=arrSubnetMasks)
    if returnValue[0] == 0 or returnValue[0] == 1:
        ip= arrIPAddresses
        return ip
    return 0



def exit():
    exit = input('按任意键退出')
    if exit:
        sys.exit()



if __name__ == '__main__':
    changip = changip()
    if changip:
        print('修改成功:', "ip为:", changip[0])
    else:
        print('修改失败,请以管理员权限运行')
    exit()