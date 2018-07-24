
import os

fn= os.path.join(os.path.dirname(__file__), 'source/write.txt')


# with open(fn,'wt') as f:
#     print('Hello world!',file=f)


# print(1,2,3,4,5,sep=',',end='!!!\n')


for i in range(5):
    print(i,end=' ')