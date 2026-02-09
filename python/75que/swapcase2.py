#write a program to swap the case of each character in a string. For example, if the input string is "PyThOn", the output should be "pYtHoN".
#using built-in function
a="PyThOn"
result=""
for char in a:
    if char.islower():
        result+=char.upper()
    else:
        result+=char.lower()
print(result)

#using built-in function
a="PyThOn"
result=a.swapcase()
print(result)

#using list comprehension
a="PyThOn"
result="".join([char.lower() if char.isupper() else char.upper() for char in a])
print(result)

#using map and lambda function
a="PyThOn"
result="".join(map(lambda char: char.lower() if char.isupper() else char.upper(), a))
print(result)
