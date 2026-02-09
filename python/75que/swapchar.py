# Write a Python program to swap the case of each character in the string "pyThOn" and print the result.
#using for loop and if condition
a="pyThOn"
result=""
for char in a:
    if char.islower():
        result+=char.upper()
    else:
        result+=char.lower()
print(result)

#using list comprehension
a="pyThOn"
result="".join([char.upper() if char.islower() else char.lower() for char in a])
print(result)

#using built-in method
a="pyThOn"
result=a.swapcase()
print(result)

#using lambda function and map
a="pyThOn"
result="".join(map(lambda char: char.upper() if char.islower() else char.lower(), a))
print(result)


