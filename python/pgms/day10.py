'''#list comprehension
#wap to print the even number with help of list
lst1=[1,2,3,4,5,6,7,8,9,10]
print(lst1)
lst2=[]
for i in lst1:
    if i%2==0:
        lst2.append(i)
print(lst2)

'''
'''
squares=[i**2 for i in range(1,11)]
print(squares)'''

'''#list_variable=[expression looping stmt condition stmt]
lst1=[1,2,3,4,5,6,7,8,9,10]
print(lst1)
lst2=[i for i in lst1 if i%2==0]
print(lst2)
'''
'''
#2.wap with and without LC
#Without LC
#ip->[10,2.5,2+3j,40,true,'abcd',20,50]
#op->[10,40,20,50]
lst1=[10,2.5,2+3j,40,True,'abcd',20,50]
print(lst1)
lst2=[]
for i in lst1:
    if type(i)==int:
        lst2.append(i)
print(lst2)'''

"""#with LC
lst1=[10,2.5,2+3j,40,True,'abcd',20,50]
print(lst1)
lst2=[i for i in lst1 if type(i)==int] 
print(lst2)"""

'''#3
#ip->[1,2,3,4,5,6,7,8,9,10]
#op->[[6,8,10]
#with LC
lst1=[1,2,3,4,5,6,7,8,9,10]
print(lst1)
lst2=[i for i in lst1 if i%2==0 and i>5]
print(lst2)

#without LC
lst1=[1,2,3,4,5,6,7,8,9,10]
print(lst1)
lst2=[]
for i in lst1:
    if i%2==0 and i>5:
        lst2.append(i)
print(lst2)'''

#no print stmts or genric stmts allowed in comprehension
#ip->[1,2,3,4]
#hint [1,1+2,1+2+3,1+2+3+4]
#op->[1,3,6,10]
#without LC
'''lst1=[1,2,3,4]
print(lst1)
res=[]
data=0
for i in lst1:
    data+=i
    res.append(data)
print(res)   
#with LC
lst1=[1,2,3,4]
print(lst1)
data=0
res=[data:=data+i for i in lst1]
print(res)'''

'''#2.Fibbonaci series
#in->n=6
#op->[0,1,1,2,3,5,8,13]

n=6
prev,curr=0,1
print(f'fibo series: {prev} {curr}',end=' ')
for i in range(n):
    prev,curr=curr,prev+curr
    print(f'{curr}',end=' ')
print()'''


#with LC
'''n=6
prev,curr=0,1
fibo_series=[(prev:=curr,curr:=prev+curr)[0] for i in range(n+1)]
print(fibo_series)
'''

'''lst=[1,2,3,4,5,6]
print(lst)
data=[[lst[i],lst[i+1]] for i in range(len(lst)-1)]
print(data)
'''

import sys
print(sys.argv)
