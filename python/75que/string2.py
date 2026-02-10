# Remove spaces from the string
#using for loop and if condition
a="he llo wor ld"
result=""
for char in a:
    if char!=" ":
        result+=char
print(result)

#using list comprehension
a="he llo wor ld"
result="".join([char for char in a if char!=" "])
print(result)

