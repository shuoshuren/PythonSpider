#!/usr/bin/python

# coding=utf-8

import urllib.request

# 向指定的URL地址发送请求，返回服务器响应的类文件对象
response = urllib.request.urlopen("http://www.baidu.com")

# read（）方法就是读取文件的全部内容，返回字符串
html = response.read()

print(html)