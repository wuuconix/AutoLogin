# AutoLogin
哈尔滨工业大学（威海）校园网自动登录/自动退出python脚本

> Author: wuuconix
## 脚本原理介绍
+ 利用requests库访问[http://www.msftconnecttest.com/redirect](http://www.msftconnecttest.com/redirect)。正常情况下，会一个跳转的script标签，在这个标签里藏着校园网登录界面的url。提取后我们便得到了登陆界面的url。
+ 对登录界面进行抓包后，发现，处理登录请求的的url是[http://172.26.156.158:80/eportal/InterFace.do?method=login](http://172.26.156.158:80/eportal/InterFace.do?method=login)，我们只需要用post方式向这个界面传值就行(具体传了什么值见脚本，你只需要输入账号和密码即可)
+ 同理，处理退出请求的url在抓包后发现是[http://172.26.156.158:80/eportal/InterFace.do?method=logout](http://172.26.156.158:80/eportal/InterFace.do?method=logout)
+ 登录成功后，界面会返回一个userIndex，是学生的唯一标识，这里用文件操作把它保存到了目录下userIndex这个文件中(退出功能需要用到这个userIndex)
+ 这个userIndex的貌似有规律，所有学生的前95位都是一致的，后面是混淆后的学号，根据这一点，smartlogin.py会根据用户输入的学号自动生成userIndex，从而达到退出登入的功能。

## 脚本使用
+ 登录
```python
python3 login.py
```
+ 退出
```python
python3 logout.py
```

## 脚本使用注意事项
+ 在运行login.py之前请确保当前的校园网是没有登录的，试着手动下线
+ 如果手动下线有困难，试着运行以下代码智能退出。
```python
python3 smartlogin.py
```
+ 因为logout.py需要从userIndex这个文件里读内容，而这个文件是login.py生成的。所以只有成功利用脚本登录后才能利用logout.py脚本下线。
+ logout.py和smartlogout.py唯一的区别就是，userIndex一个是从login.py生成出来的userIndex文件里读出来的，这个userIndex因为是直接从网页抓下来的，一定正确。而smartlogout.py的userIndex是根据输入的学号直接生成的，可能会有问题。