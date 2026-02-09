#Write a Python program to extract digits from a given string and print them as a single string.
#using for loop and if condition
a="a1b2c3d44"
result=""
for char in a:
    if char.isdigit():
        result+=char
print(result)

#using list comprehension
a="a1b2c3d44"
result="".join([char for char in a if char.isdigit()])
print(result)

