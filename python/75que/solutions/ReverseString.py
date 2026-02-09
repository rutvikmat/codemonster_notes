#Pythonic way to reverse a string.
ip="python"
op=ip[::-1]
print(op)

#Using reversed()
ip="python"
op=''.join(reversed(ip))
print(op)

#using for loop
ip="python"
op=""
for char in ip:
    op=char+op
print(op)

#using while loop
ip="python"
op=""
i=len(ip)-1
while i>=0:
    op+=ip[i]
    i-=1
print(op)
