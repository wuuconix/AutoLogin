import requests

try:
    with open("userIndex", "r") as f:
        userIndex = f.read()
    burp0_url = "http://172.26.156.158:80/eportal/InterFace.do?method=logout"
    burp0_cookies = {"EPORTAL_COOKIE_OPERATORPWD": "", "EPORTAL_COOKIE_USERNAME": "", "EPORTAL_COOKIE_PASSWORD": "", "EPORTAL_COOKIE_SERVER": "", "EPORTAL_COOKIE_SERVER_NAME": "", "EPORTAL_AUTO_LAND": "", "EPORTAL_USER_GROUP": "null", "JSESSIONID": "B58CA79A93685AB132111D8E5B2B21C2"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0", "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "http://172.26.156.158", "Connection": "close", "Referer": "http://172.26.156.158/eportal/success.jsp?userIndex=" + userIndex}
    burp0_data = {"userIndex": userIndex}
    response = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    response.encoding = response.apparent_encoding
    print(response.text)
except Exception:
    print("宁还未使用login.py登陆过，没有userIndex文件，尝试运行smartlogout.py智能退出")
