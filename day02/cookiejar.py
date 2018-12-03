#!/usr/bin/python

import urllib.request
import urllib.parse
import http.cookiejar

# 创建cookie对象,保存cookie
cookie = http.cookiejar.CookieJar()

#构建处理器对象，用来处理cookie
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(cookie_handler)

data = {
	"email":"mr_mao_hacker@163.com",
	"password":"alarmchime"
}

url = "http://www.renren.com/PLogin.do"

# 通过urlencode转码
data = urllib.parse.urlencode(data).encode("utf-8")

request = urllib.request.Request(url,data = data)

# 发送第一次post请求，生成登录后的cookie(如果成功)
response = opener.open(request)

# 第二次请求，将保存生成的cookie一并发到web服务器，服务器会验证cookie通过
response_deng = opener.open("http://www.renren.com/410046129/profile")

print(response_deng.read())