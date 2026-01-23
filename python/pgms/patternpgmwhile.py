"""
n = int(input("Enter number of rows: "))
i = 1

while i <= n:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

op->
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 

n = int(input("Enter number of rows: "))
i = n

while i >= 1:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i -= 1

op->
Enter number of rows: 5
* * * * * 
* * * * 
* * * 
* * 
*

n = 5
i = 1

while i <= n:
    space = n - i
    while space > 0:
        print(" ", end="")
        space -= 1

    star = 1
    while star <= i:
        print("* ", end="")
        star += 1

    print()
    i += 1
op->

    *
   * *
  * * *
 * * * *
* * * * *

n = 5
i = 1

while i <= n:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1
op->
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
"""
n = int(input("Enter number of rows: "))
i = n

while i >= 1:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i -= 1"""