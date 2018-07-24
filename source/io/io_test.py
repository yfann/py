
import os

fn = os.path.join(os.path.dirname(__file__), 'source/sample.txt')
fn1 = os.path.join(os.path.dirname(__file__), 'source/write.txt')
fb = os.path.join(os.path.dirname(__file__), 'source/sample.bin')

# with open(fn,'rt') as f:
#     data=f.read()
#     print(data)


# with open(fn,'rt') as f:
#     for line in f:
#         print(line)


# with open(fn1,'wt') as f:
#     f.write('abc')
#     f.write('123')

# with open(fn1,'at') as f:
#     f.write('abc')
#     f.write('123')

# f = open('fn', 'rt')
# data = f.read()
# f.close()


# with open(fb,'wb') as f:
#     f.write(b'hello world')

with open(fb, 'rb') as f:
    data = f.read(16)
    print(data)
    print(data.decode('utf-8'))

# with open(fb, 'wb') as f:
#     text = 'Hello World'
#     f.write(text.encode('utf-8'))
