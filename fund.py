import requests
import time
import os
import json

# 001938 161725 166008 000961 000011 001163

fund = []
while True:
    os.system('cls')
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/70.0.3538.110 Safari/537.36"}
    arr = ["001938", "161725", "166008", "000961", "000011", "001163"]
    for a in arr:
        url = "http://fundgz.1234567.com.cn/js/" + a + ".js"
        html = requests.get(url=url, headers=headers).content.decode('utf8')
        result = html.split(',')
        fund.append(
            result[6][10:-4] + "   " + result[5][9:-1] + "%" + "    " + result[1][8:-1] + "(" + result[0][21:-1] + ")")
        time.sleep(0.1)
    for x in fund:
        print(x)
    fund = []
    time.sleep(10)
