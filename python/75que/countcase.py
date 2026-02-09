# Count the number of uppercase and lowercase letters in the string "AbC12dE" and print the results.
#using for loop and if condition
a="AbC12dE"
uppercase=0
lowercase=0
for char in a:
    if char.isupper():
        uppercase+=1
    elif char.islower():
        lowercase+=1
print("uppercase =", uppercase, "lowercase =", lowercase)

#using list comprehension
a="AbC12dE"
uppercase=sum(1 for char in a if char.isupper())
lowercase=sum(1 for char in a if char.islower())
print("uppercase =", uppercase, "lowercase =", lowercase)

