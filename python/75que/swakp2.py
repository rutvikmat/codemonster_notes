#swap the case of each character in the string "PYTHON" and print the result.
#using for loop and if condition
a="PYTHON"
result=""
for char in a:
    if char.isupper():
        result+=char.lower()
    else:
        result+=char.upper()
print(result)

#using list comprehension
a="PYTHON"
result="".join([char.lower() if char.isupper() else char.upper() for char in a])
print(result)

