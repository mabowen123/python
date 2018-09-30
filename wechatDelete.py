#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author :mabowen
# @Time   :2018/8/15 19:56
import itchat, time
"""
检测微信单删
"""
# 登陆
itchat.auto_login()
# 获取好友列表
friendList = itchat.get_friends(update=True)[1:]
num = [0, 1]


def send(g, num):
    itchat.send('ॣ ॣ ॣ', friendList[g + num]['UserName'])
    print((friendList[g + num]['RemarkName'] or friendList[g + num]['NickName']), '已发送')


itchat.send('正在开始测试', 'filehelper')
# 预估时间
needtime = round(1 + int(len(friendList)) / 2 / 60, 2)
itchat.send('共' + str(len(friendList)) + '人' + '\n预计需要' + str(needtime) + 'min', 'filehelper')
# 循环给各个好友发送信息,1s发两条
for g in range(0, len(friendList), 2):
    for i in num:
        if g + i < len(friendList):
            # 发送特殊字符
            send(g, i)
            print(str(g + i + 1) + "/" + str(len(friendList)) + "\r")
    # 限制频率
    time.sleep(1)

itchat.send('结束测试,请在聊天列表页查看', 'filehelper')
