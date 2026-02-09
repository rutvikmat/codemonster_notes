#write a python program to remove duplicate characters from a string and print the result.
#using for loop and if condition
a="banana"
result=""
for char in a:
    if char not in result:
        result+=char
print(result)

#using set and join
a="banana"
result="".join(set(a))
print(result)

#using dictionary
a="banana"
result=""
char_count={}
for char in a:
    if char not in char_count:
        char_count[char]=1
        result+=char
print(result)

