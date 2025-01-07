from numpy import *

a = matrix('1,2,3; 4,5,6; 7,8,9')
print(a)
print()

#  Max Values
big = a.max()
print("Maximum Value =",big)
print()

#  Mininum Values
small = a.min()
print("Minimum Value =",small)
