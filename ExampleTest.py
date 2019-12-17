# 实例
print('A', 'B')
print('Z', 'F', 'G')
name = input('请输入你的名字：')
print('hello', name)

var = 100
if (var == 100):
    print("变量var的值为100")
    print("Good bye")

from collections import Counter

text = "dada 年后 你您 当年我都 道德经澳门 解决房价 ii 哦 没 跑跑 年后"
words = text.split()
print(words)

counter = Counter(words)
topThree = counter.most_common(3)# 出现次数最多的三个元素 没有特定顺序 （获取字符串中最常见的文字）
print(topThree)
