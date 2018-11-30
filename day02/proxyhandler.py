#!/usr/bin/python

import urllib.request

# 代理开关，表示是否启用代理
proxyswitch = False

# 构建一个handler处理器对象，参数是字典类型，包括代理类型和dialing服务器ip+prot
httpproxy_handler = urllib.request.ProxyHandler({"http":"124.88.67.54:80"})

# 构建一个没有代理的处理器对象
nullproxy_handler = urllib.request.ProxyHandler({})

if proxyswitch:
	opener = urllib.request.build_opener(httpproxy_handler)
else:
	opener = urllib.request.build_opener(nullproxy_handler)

# 构建一个全局的opener，之后的所有的请求都可以用urlopen方式去发送
urllib.request.install_opener(opener)

request = urllib.request.Request("http://www.baidu.com")

response = urllib.request.urlopen(request)

print(response.read())