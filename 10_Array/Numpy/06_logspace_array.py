from numpy import *

a = logspace(1,4,5)
# print(a)
n = len(a)
print(n)

for i in range(n):
    print('%.1f' % a[i], end=',')