str = "Core Python"

n = len(str)
print(n)

# Positive Indexing 
i = 0
while i<n:
    print(str[i],end=' ')
    i+=1
print()

# Negative Indexing 
i = -1
while i >= -n:
    print(str[i],end=" ")
    i-=1
print()

# Negative Indexing
i = 1
n = len(str)
while i<=n:
    print(str[-i],end=" ")
    i+=1
