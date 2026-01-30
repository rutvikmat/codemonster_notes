"""lst = [10,2.5,'hi']
print(lst)
lst[1]=90
print(lst)
lst.append('hello')
print(lst)"""
"""
range(10)
print(list(range(10)))
range(3,10)
print(list(range(3,10)))
range(3,10,2)
print(list(range(3,10,2)))
a=list(range(10,3,-1))
print(list(range(10,3,-1)))
print(a)"""

"""n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print("* ",end="")
    print()
    
n=5
for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(n-i+1):
        print("* ",end="")
    print()

n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

n = 5
for i in range(n):
    for j in range(i, n-1):   # spaces
        print(' ', end=' ')
    for j in range(i+1):      # stars
        print('*', end=' ')
    print()


n = 5
for i in range(n):
    for j in range(i, n-1):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print()
"""

n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i+1,n):
        print("*",end=" ")
    print()