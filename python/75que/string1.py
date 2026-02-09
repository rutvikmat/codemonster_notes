# Remove spaces from the string
#using for loop
a="hello world python"
result=""
for char in a:
    if char==" ":
        result+="-"
    else:
        result+=char
print(result)

#using while loop
a="hello world python"
result=""
i=0
while i<len(a): 
    char=a[i]
    if char==" ":
        result+="-"
    else:
        result+=char
    i+=1
print(result)

#using list comprehension
a="hello world python"
result=''.join(['-' if char==" " else char for char in a])
print(result)
