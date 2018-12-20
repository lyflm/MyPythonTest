import json
import time
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def login():
    url = 'http://www.zhihu.com'
    loginURL = 'http://www.zhihu.com/login/email'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
        "Referer": "http://www.zhihu.com/",
        'Host': 'www.zhihu.com',
    }
    data = {
        'email': 'feilong_ma@163.com',
        'password': 'Fl523571',
        'rememberme': "true",
    }
    global s
    s = requests.session()
    global xsrf

    req = s.get(url, headers=headers)
    print(req)
    soup = BeautifulSoup(req.text, "html.parser")
    xsrf = soup.find('input', {'name': '_xsrf', 'type': 'hidden'}).get('value')
    data['_xsrf'] = xsrf
    timestamp = int(time.time() * 1000)
    captchaURL = 'http://www.zhihu.com/captcha.gif?=' + str(timestamp)
    print(captchaURL)
    with open('zhihucaptcha.gif', 'wb') as f:
        captchaREQ = s.get(captchaURL, headers=headers)
        f.write(captchaREQ.content)
    loginCaptcha = input('input captcha:\n').strip()
    data['captcha'] = loginCaptcha
    print(data)
    loginREQ = s.post(loginURL, headers=headers, data=data)

    if loginREQ.status_code == 200:
        print('login success')
    else:
        print('login fail')

login()