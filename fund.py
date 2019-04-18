import requests
import time
import os
import threading


# 001938 161725  000961 000011 001163
def get(code):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/70.0.3538.110 Safari/537.36"}
    url = "http://fundgz.1234567.com.cn/js/" + code + ".js"
    html = requests.get(url=url, headers=headers).content.decode('utf8')
    result = html.split(',')
    print(
        result[6][10:-4] + "   " + result[5][9:-1] + "%" + "    " + result[1][8:-1] + "(" + result[0][21:-1] + ")")


def threads(t_group):
    thread = []
    for t in t_group:
        thread.append(threading.Thread(target=get, args=(t,), name=t))

    return thread


t_group = ["470007","161032","001052","001630","001938", "161725", "000961", "001163"]
while True:
    os.system('cls')
    for t in threads(t_group):
        t.start()
        t.join()

    time.sleep(20)

