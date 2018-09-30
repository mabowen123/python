#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author :mabowen
# @Time   :2018/8/15 19:56
import itchat, time

# 登陆
itchat.auto_login()
# 获取好友列表
friendList = itchat.get_friends(update=True)
print(friendList)