#!/usr/bin/python

import urllib.request

test = "test"

password = "123456"

webserver = "192.168.21.52"

# 构建一个密码管理对象，可以用来保存和http相关的授权账户信息
passwordMgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# 添加授权账户信息，第一个参数realm如果没有就写None,后三个参数分别为站点 Ip,账户，密码
passwordMgr.add_password(None,webserver,test,password)

httpauth_handler = urllib.request.HTTPBasicAuthHandler(passwordMgr)

opener = urllib.request.build_opener(httpauth_handler)

request = urllib.request.Request("http://"+webserver)

response = opener.open(request)

print(response.read())