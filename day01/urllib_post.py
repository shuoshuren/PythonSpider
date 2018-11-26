#!/usr/lib/python

import urllib.request
import urllib.parse

url = "http://fanyi.youdao.com/translate?smartresult=dict"
headers = {"User-Agent":"Mozilla"}

key = input("请输入要翻译的文字：")

formdata={
    "type":"AUTO",
    "i":key,
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"UTF-8",
    "action":"FY_BY_CLICKBUTTON",
    "typeResult":"true"
}

data = urllib.parse.urlencode(formdata).encode("utf-8")

request = urllib.request.Request(url,data=data,headers = headers)

response = urllib.request.urlopen(request)

print(response.read())