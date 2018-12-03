#!/usr/bin/python

import re

# 匹配数字
regex = r"\d+"

regex = r"([a-z]+) ([a-z]+)"

# re.I 表示忽略大小写
# re.S 表示全文匹配
pattern = re.compile(regex,re.I)

m = pattern.match("hello world hello Python")

print(m.group(0))

print(m.group(1))

print(m.group(2))