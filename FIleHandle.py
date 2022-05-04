from asyncore import read, write


# r read
# w write
# t text
# b binary

fileDemo = open('note.txt', 'wt')
fileDemo.write('Say hi!!!!!!!!!!')
fileDemo.close()

fileDemo = open('note.txt', 'rt')
content = fileDemo.read()
fileDemo.close()
print(content)