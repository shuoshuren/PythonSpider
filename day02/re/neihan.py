#!/usr/bin/python

import urllib.request
import re

class Spider:
    def __init__(self):
        self.page = 1
        # 爬取开关
        self.switch = True
        pass

    def loadPage(self):
        """
        下载页面
        """
        url = "http://www.neihan8.com/article/list_5_"+str(self.page)+".html"
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36"}
        request = urllib.request.Request(url,headers = headers)
        response = urllib.request.urlopen(request)
        # 每页的HTML源码
        html = response.read().decode("GBK")

        # 创建一个正则表达式规则
        pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>',re.S)
        # 返回结果
        content_list = pattern.findall(html)
        
        self.dealPage(content_list)

    def dealPage(self,content_list):
        """
        处理每页的段子
        """
        for content in content_list:
            content = content.replace("<p>","").replace("</p>","").replace("<br />","")
            self.writePage(content) 

        

    def writePage(self,content):
        """
        把每条段子逐个写入文件里
        """
        with open("duanzi.txt","a") as f:
            f.write(content)

    def startWork(self):
        """
        控制爬虫运行
        """
        while self.switch:
            self.loadPage()
            command = input("继续爬取，亲按回车，退出输入quit:")
            if command == "quit":
                self.switch = False
            
            self.page += 1

if __name__ == "__main__":
    duanzi = Spider()
    duanzi.startWork()
