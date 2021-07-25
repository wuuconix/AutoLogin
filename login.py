import requests
from urllib import parse
import json

from requests.models import Response

response = requests.get("http://www.msftconnecttest.com/redirect").text
if (response[:31] != "<script>top.self.location.href="):    #查看是否正常跳转
    print("无法跳转，可能的原因是你现在已经连着校园网，请手动退出后重试，或者运行smartlogout.py智能退出")
else:
    login_url = response[32:-12]    #访问微软官方重定向网站，获得跳转信息，从响应中分理处校园网登陆界面url
    queryString = parse.quote(login_url[40:])   #对url后面跟着的一些参数进行一次url编码，之后登录的时候需要post

    while True:
        print("请输入你的学号:")
        username = input()
        print("请输入你的校园网密码:")
        password = input()
        burp0_url = "http://172.26.156.158:80/eportal/InterFace.do?method=login"    #处理登录请求的url，我们需要对它进行post请求
        burp0_cookies = {"EPORTAL_COOKIE_OPERATORPWD": "", "EPORTAL_COOKIE_USERNAME": "", "EPORTAL_COOKIE_PASSWORD": "", "EPORTAL_COOKIE_SERVER": "", "EPORTAL_COOKIE_SERVER_NAME": "", "EPORTAL_AUTO_LAND": ""}
        burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0", "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "http://172.26.156.158", "Connection": "close", "Referer": login_url}
        burp0_data = {"userId": username, "password": password, "service": '', "queryString": queryString, "operatorPwd": '', "operatorUserId": '', "validcode": ''}
        response = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
        response.encoding = response.apparent_encoding
        print(response.text)
        userIndex = json.loads(response.text)['userIndex']
        if (userIndex):
            with open ("userIndex", "w") as f:
                f.write(userIndex)
            print("登录成功, enjoy it！")
            break
    
