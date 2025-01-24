id = 26893
Name = "Siddhant Gautam"
salry = 54000

print("{}, {}, {}".format(id,Name,salry))
print()
print("{0},{1},{0}".format(id,Name,salry))
print()
print("{}\n{}\n{}\n".format(id,Name,salry))

print("Id={one}, Name = {two}, Salry = {three}".format(one = id, two = Name, three = salry))
print()

print("Id={:d}, Name={:s}, Salary={:2f}".format(id,Name,salry))

num = 5000
print("{:*>15d}".format(num))
print("{:*^15d}".format(num))

# Hexadecimal or Binar number
n1 = 1000
print("Hexadecimal {:.>15x}\nBinary {:.>15b}".format(n1,n1))
print("Hexadecimal {:.>#15x}\nBinary {:.<#15b}".format(n1,n1))


