#!/usr/bin/python

# coding=utf-8

import urllib.request

# 通过urllib.Request()方法构造一个请求对象
'''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cache-Control: max-age=0
Connection: keep-alive
Cookie: BAIDUID=6EF80C8B11D09EEB5959821488E62CA8:FG=1; BIDUPSID=6EF80C8B11D09EEB5959821488E62CA8; PSTM=1538138173; BD_UPN=123353; BDUSS=tWazZON0Z4NmRmcDR2cDJTR2pwaW9VcmQ2WVZZeHdsSmJ0RUdjUDFwZHpWLWxiQVFBQUFBJCQAAAAAAAAAAAEAAAAIPWgxeGM1MzQzNjExMjQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHPKwVtzysFbTU; MCITY=-75%3A; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; H_PS_PSSID=1454_21119_20691_27376_26350_27509; H_PS_645EC=d777hqh9TH%2Flz%2BPmj%2BGutYJzRwuxYfGD6ySoyR2peJGl4Y788WxYiHnXRzTjPQHBxwRc
Host: www.baidu.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36
'''
# User-Agent 是爬虫和反爬虫斗争的第一步
ua_headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}

url = "http://www.baidu.com"

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"

request = urllib.request.Request(url,headers=ua_headers)

# 添加/修改一个HTTP 报头
request.add_header("User-Agent",user_agent)

# 向指定的URL地址发送请求，返回服务器响应的类文件对象
response = urllib.request.urlopen(request)

# read（）方法就是读取文件的全部内容，返回字符串
html = response.read()

# 返回http响应码
code = response.getcode()

# 返回实际的URL地址，防止重定向
url = response.geturl()

# 服务器响应的HTTP包头
info = response.info()

print(request.get_header("User-agent"))
