# coding: UTF-8

import sys
print(sys.getdefaultencoding())

print(type('中文'))
print(type(u'中文'))
print(type(u'中文'))
print(u'中文'.encode('gbk'))
#print('中文'.decode())
#print(u'中文'.encode())

#python3
str1 = '\u4f60\u597d'  
print(str1.encode().decode('unicode_escape'))
print(str1)