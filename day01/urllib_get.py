#!/usr/lib/python

import urllib.parse
import urllib.request

url = "http://www.baidu.com/s"

headers = {"User-Agent":"Mozilla"}

keyword = input("请输入要查询的字符串:\n")

wd = {"wd":keyword}

# 通过urllib.parse.urlencode 转码
wd = urllib.parse.urlencode(wd)

fullurl = url + "?"+ wd

print("%s" %fullurl)
request = urllib.request.Request(fullurl,headers = headers)

response = urllib.request.urlopen(request)

print(response.read())