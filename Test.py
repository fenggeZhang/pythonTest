
import re
pattern =re.compile(r'\d+')            #用于匹配至少一个数字
m=pattern.match('one12twothree34four') #查找头部，没有匹配
print(m,'\n')
m=pattern.match('one12twothree34four',2,10) #从脚标为2的‘e’开始匹配，并没有匹配
print(m)
m=pattern.match('one12twothree34four',3,10) #从脚标为3的‘1’开始匹配，正好匹配
print(m) # <re.Match object; span=(3, 5), match='12'>
print(m.group(0))
print(m.start(0))
print(m.end(0))
print(m.span(0))
print(m.groups())



