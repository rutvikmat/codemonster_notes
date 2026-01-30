"""
1. Diamond Pattern
   *
  * *
 * * *
  * *
   *

n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    print("* "*(i+1))
for i in range(n-1):
    for j in range(i+1):
        print(" ", end="")
    print("* "*(n-i-1))
"""
"""
2. Find second largest number

Input:
[10, 20, 4, 45, 99]
Output:
45
"""
lst=[10, 20, 4, 45, 99]
for i in range(len(lst)):
    if lst[i]==max(lst):
        lst.remove(lst[i])
        break
print(max(lst))
"""
"""
'''
3. Check if two strings are anagrams

Input:
"listen", "silent"
Output:
Anagram

str1 = "listen"
str2 = "silent"
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")
'''