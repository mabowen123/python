#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author :mabowen
# @Time   :2018/9/29 16:28
import random
"""
生成一个随机数,猜中数字
"""

def game():
    count = 1
    userNum = userIput()
    while 1:
        if userNum == num:
            print('恭喜你猜中了')
            print('一共用了' + str(count) + '次')
            bool = input('任意键退出')
            if bool:
                exit('bye')
        elif userNum > num:
            print('大了')
            count += 1
            userNum = userIput()
        elif userNum < num:
            print('小了')
            count += 1
            userNum = userIput()


def userIput():
    userNum = input('请输入你猜得数字1到10000:')
    userNum = int(userNum)
    return userNum


if __name__ == '__main__':
    num = random.randint(0, 10000)
    game()
