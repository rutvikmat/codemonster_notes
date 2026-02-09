#using stack
a="python is fun"
stack=[]
for char in a:
    stack.append(char)
    result=""
while stack:
    result+=stack.pop()
print(result)   