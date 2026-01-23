"""
Docstring for python.pgms.pattern_pgm
pattern programming
-----------------------
pattern-1
----------
print('*')

op
---
*


pattern-2
-----------

n=5
for i in range(n):
	print('*')


op
---

*
*
*
*
*

#pattern-3
----------
* * * * * 


n=5
for i in range(n):
	print('*',end=' ')

pattern-4
------------
n=5
for i in range(n):#rows
	for j in range(n):#col
		print('*',end=' ')
		
op
---
* * * * * * * * * * * * * * * * * * * * * * * * *


pattern-5
-----------

n=5
for i in range(n):#rows
	for j in range(n):#col
		print('*',end=' ')
	print()


op
---

* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 


pattern-6
----------
n=5
for i in range(n): #rows
	for j in range(i+1): #col
		print('*',end=' ')
	print()


op
---
*
* *
* * *
* * * *
* * * * *
rows=5
col=5
star=depend on rows

patter-7
-----------
* * * * *
* * * * 
* * * 
* * 
* 

row=5
col=5
star= reverse of rows



task:
------
patter-8
-----------
    *
   * * 
  * * * 
 * * * *
* * * * *

n=5
for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for k in range(i+1):
        print('* ', end='')
    print()
patter-9
---------
* * * * *    
 * * * *
  * * *
   * *
    *

n=5
for i in range(n): # rows
    for j in range(i):
        print(' ', end='')
    for k in range(n-i):
        print('* ', end='')
    print()
    """