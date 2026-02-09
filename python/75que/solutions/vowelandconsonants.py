#using for loop
a = "beautiful"
vowels = 0
consonants = 0
for char in a:
    if char in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
print("vowels =", vowels, "consonants =", consonants)

#using while loop
a = "beautiful"
vowels = 0
consonants = 0
i = 0
while i < len(a):
    char = a[i]
    if char in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    i += 1
print("vowels =", vowels, "consonants =", consonants)

#using list comprehension
a = "beautiful"
vowels = sum(1 for char in a if char in "aeiou")
consonants = sum(1 for char in a if char.isalpha() and char not in "aeiou")
print("vowels =", vowels, "consonants =", consonants)

#using collections.Counter
from collections import Counter
a = "beautiful"
counter = Counter(a)
vowels = sum(counter[char] for char in "aeiou")
consonants = sum(counter[char] for char in counter if char.isalpha() and char not in "aeiou")
print("vowels =", vowels, "consonants =", consonants)
print(counter)

#using regex
import re
a = "beautiful"
vowels = len(re.findall(r'[aeiou]', a))
consonants = len(re.findall(r'[bcdfghjklmnpqrstvwxyz]', a, re.IGNORECASE))
print("vowels =", vowels, "consonants =", consonants)




# Remove the vowels from the string "knowledge" and print the result.
#using for loop and if condition
a="knowledge" 
result=""
for char in a:
    if char not in "aeiou":
        result+=char
print(result)

#using list comprehension
a="knowledge"
result=''.join([char for char in a if char not in "aeiou"])
print(result)

#using filter and lambda function
a="knowledge"
result=''.join(filter(lambda char: char not in "aeiou", a))
print(result)

#using while loop and if condition
a="knowledge"
result=""
i=0
while i<len(a):
    char=a[i]
    if char not in "aeiou":
        result+=char
    i+=1
print(result)
