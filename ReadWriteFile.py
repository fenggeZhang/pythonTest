fw = open('sample.txt', 'w')
fw.write('我是第一行\n')
fw.write('i am excellent')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()
