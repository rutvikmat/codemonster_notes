"""
s='learning python is easy'
for i in range(len(s)):
    print(s[i],end='')
print()

for i in range(len(s)):
    print(s[-i-1],end='')

#print the str in forward and reverse direction using while loop

"""
'''
s='learning python is easy'
i=0
while i<len(s):
    print(s[i],end='')
    i+=1
print()
s='learning python is easy'
i=len(s)-1
while i>=0:
    print(s[i],end='')
    i-=1
print()

'''
#task-2 
# print +ve char -ve index number of given str using both for loop and while loop
s='learning python is easy'
for i in range(len(s)):
    print(i,s[i],i-len(s))
print()

i=0
while i<len(s):         
    print(i,s[i],i-len(s))
    i+=1