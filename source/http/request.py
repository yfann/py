from urllib.request import urlopen

u=urlopen('http://localhost:15000/aa.txt')
print(u)
data=u.read().decode('utf-8')
print(data)