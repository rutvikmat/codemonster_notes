#write a python program to reverse the string "python is fun" without using slicing or built-in functions.
#using for loop and if condition
a="python is fun"
result=""
for char in a:
    if char!=" ":
        result=char+result
    else:
        result=char+result
print(result)

#using list and join
a="python is fun"
result="".join(reversed(a))
print(result)

#using stack
a="python is fun"
stack=[]
for char in a:
    stack.append(char)
    result=""
while stack:
    result+=stack.pop()
print(result)   
