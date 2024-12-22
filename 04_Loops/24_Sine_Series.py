x,n = [int(i) for i in input("Enter angle value, no. of iterations : ").split(',')]

r = (x*3.14159)/180

t = r

sum = r
print('Iteration = %d\t Sum = %f' % (1,sum))

i = 2

for j in range(2, n+1):
    t = (-1)*t*r*r/(i*(i+1))
    sum = sum + t
    print('Iteration = %d\tSum = %f' % (j, sum))
    i+=2

