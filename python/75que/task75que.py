"""STRING QUESTIONS (ip = , req op = )
BASIC (1–15)
1.
ip = "python"
req op = "nohtyp"
solution:

ip="python"
op=ip[::-1]
print(op)

2.
ip = "beautiful"
req op = vowels = 5, consonants = 4

a="beautiful"
vowels=0
consonants=0
for char in a:
    if char in "aeiou":
        vowels+=1
    elif char.isalpha():
        consonants+=1
print("vowels =", vowels, "consonants =", consonants)

3.
ip = "knowledge"
req op = "knwldg"

a="knowledge" 
result=""
for char in a:
    if char not in "aeiou":
        result+=char
print(result)

4.
ip = "madam"
req op = "palindrome"
"""
a="madam"
if a==a[::-1]:
    print("palindrome")
else:    
    print("not palindrome")
"""
5.
ip = "a1b2c3d44"
req op = "12344"
"""
a="a1b2c3d44"
result=""
for char in a:
    if char.isdigit():
        result+=char
print(result)
"""
6.
ip = "AbC12dE"
req op = uppercase=3, lowercase=3
"""
a="AbC12dE"
uppercase=0
lowercase=0
for char in a:
    if char.isupper():
        uppercase+=1
    elif char.islower():
        lowercase+=1
print("uppercase =", uppercase, "lowercase =", lowercase)
"""

7.
ip = "he llo wor ld"
req op = "helloworld"
"""
a="he llo wor ld"
result=""
for char in a:
    if char!=" ":
        result+=char
print(result)
"""
8.
ip = "hello world python"
req op = "hello-world-python"
"""
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

"""
9.
ip = "success", char = 's'
req op = 3
"""
a="success"
char='s'
count=0
for c in a:
    if c==char:
        count+=1
print(count)
"""
10.
ip = "abc"
req op =
a 97
b 98
c 99
"""
a="abc"
for char in a:
    print(char, ord(char))

"""
11.
ip1 = "listen", ip2 = "silent"
req op = "anagram"

"""
a1="listen"
a2="silent"
if sorted(a1)==sorted(a2):
    print("anagram")
else:
    print("not anagram")
"""

12.
ip = "pyThOn"
req op = "PYTHON"
"""
a="pyThOn"
result=""
for char in a:
    if char.islower():
        result+=char.upper()
    else:
        result+=char.lower()
print(result)
"""

13.
ip = "PYTHON"
req op = "python"
"""
a="PYTHON"
result=""
for char in a:
    if char.isupper():
        result+=char.lower()
    else:
        result+=char.upper()
print(result)
"""
14.
ip = "banana"
req op = "ban"
"""
a="banana"
result=""
for char in a:
    if char not in result:
        result+=char
print(result)
"""

15.
ip = "python java javascript"
req op = "javascript"
"""
a="python java javascript"
words=a.split()
longest_word=""
for word in words:
    if len(word)>len(longest_word):
        longest_word=word
print(longest_word)



"""
INTERMEDIATE (16–30)
16.
ip = "python is fun"
req op = "nohtyp si nuf"
"""
a="python is fun"
result=""
for char in a:
    if char!=" ":
        result=char+result
    else:
        result=char+result
print(result)

"""

17.
ip = "PyThOn"
req op = "pYtHoN"
""" 
a="PyThOn"
result=""
for char in a:
    if char.islower():
        result+=char.upper()
    else:
        result+=char.lower()
print(result)
"""
18.
ip = "mississippi"
req op = {m:1, i:4, s:4, p:2}
"""
a="mississippi"
freq={}
for char in a:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)

"""
19.
ip = "aabbccde"
req op = "d"

ip = "aabbccde"
char=""
for char in ip:
    if ip.index(char) == ip.rindex(char):
        print(char)
        break


20.
ip = "abacbd"
req op = "a"
ip = "aabbccde"

for char in ip:
    if ip.count(char) > 1:
        print(char)
        break
21.
ip1 = "abcd", ip2 = "123"
req op = "a1b2c3d"
22.
ip = "123456"
req op = True
23.
ip = "I love Python"
req op = 3 words
24.
ip = "cabd"
req op = "abcd"
25.
ip = "programming"
req op = "progamin"
26.
ip = "he@llo#12$"
req op = "hello12"
27.
ip = "abcdef"
req op = even index = ace, odd index = bdf
28.
ip = "success"
req op = "s"
29.
ip = "a1@b2$c3"
req op = alphabets = ab c, digits = 123, special = @ $
30.
ip = "I love Python"
req op = "Python love I"
ADVANCED (31–40)
31.
ip = "education"
req op = "dc*t**n"
32.
ip = "A1 B2 C3"
req op = alphabets=3, digits=3, spaces=2
33.
ip1 = "abcde", ip2 = "cdeab"
req op = "rotation"
34.
ip = "abc"
req op =
a
ab
abc
b
bc
c
35.
ip = "aabcddd"
req op = second most repeated = "a"
36.
ip = "a3b2"
req op = "aaabb"
37.
ip = "aaabbc"
req op = "a3b2c1"
38.
ip = "xyzab"
req op = "zabcd"
39.
ip = "A man, a plan, a canal: Panama"
req op = palindrome (ignoring spaces/symbols)
40.
ip = "I love love python python python"
req op = {"I":1, "love":2, "python":3}
List questions:
*BASIC LEVEL*
### *1. Sum of numbers*
*IP:* [1, 2, 3, 4]
*Req OP:* 10
### *2. Find max & min*
*IP:* [10, 5, 7, 2]
*Req OP:* max = 10, min = 2
### *3. Count even numbers*
*IP:* [1, 4, 6, 7, 9, 10]
*Req OP:* 3
### *4. Squares of numbers*
*IP:* [2, 3, 4]
*Req OP:* [4, 9, 16]
### *5. Check if element exists*
*IP:* list = [10, 20, 30], element = 20
*Req OP:* Found
### *6. Reverse without using reverse()*
*IP:* [1, 2, 3]
*Req OP:* [3, 2, 1]
### *7. Count occurrences*
*IP:* list = [1,2,3,2,2,4], element = 2
*Req OP:* 3
# *INTERMEDIATE LEVEL*
### *8. Remove duplicates*
*IP:* [1,2,2,3,1,4]
*Req OP:* [1,2,3,4]
### *9. Merge lists without +*
*IP:* a = [1,2], b = [3,4]
*Req OP:* [1,2,3,4]
### *10. Second largest number*
*IP:* [10, 2, 30, 25]
*Req OP:* 25
### *11. Separate even & odd*
*IP:* [1,2,3,4,5]
*Req OP:* even = [2,4], odd = [1,3,5]
### *12. Cumulative sum*
*IP:* [1,2,3,4]
*Req OP:* [1,3,6,10]
### *13. Rotate list*
*IP:* [1,2,3,4,5], k = 2
*Req OP:* [4,5,1,2,3]
### *14. Flatten nested list*
*IP:* [[1,2],[3,4],[5,6]]
*Req OP:* [1,2,3,4,5,6]
# *ADVANCED LEVEL*
### *15. Pair sum target*
*IP:* nums = [2,4,3,5,7,8,-1], target = 6
*Req OP:* [(2,4), (3,3), (-1,7)]
### *16. Find common elements (without using set)*
*IP:*
a = [1,2,3,4]
b = [3,4,5,6]
*Req OP:* [3,4]
### *17. Chunk list into groups of size k*
*IP:* list = [1,2,3,4,5,6,7], k = 3
*Req OP:* [[1,2,3],[4,5,6],[7]]
### *18. Frequency dictionary*
*IP:* [‘a’,‘b’,‘a’,‘c’,‘b’,‘a’]
*Req OP:* {'a':3, 'b':2, 'c':1}
### *19. Find all indices of element*
*IP:* list = [1,2,3,2,4,2], element = 2
*Req OP:* [1,3,5]
### *20. Remove all occurrences of an element*
*IP:* list = [1,2,3,2,4], element = 2
*Req OP:* [1,3,4]
Dictionary questions:
# *1. Count frequency of each element*
*Input:*
[1,2,2,3,3,3]
*Output:*
{1:1, 2:2, 3:3}
# *2. Convert two lists into a dictionary*
*Input:*
keys = ["a","b","c"]
values = [10,20,30]
*Output:*
{"a":10, "b":20, "c":30}
# *3. Find key with maximum value*
*Input:*
{"a":5, "b":10, "c":3}
*Output:*
b
# *4. Swap keys and values*
*Input:*
{"a":1, "b":2, "c":3}
*Output:*
{1:"a", 2:"b", 3:"c"}
# *5. Merge two dictionaries*
*Input:*
d1 = {"a":1}
d2 = {"b":2, "c":3}
*Output:*
{"a":1, "b":2, "c":3}
# *6. Sort dictionary by value*
*Input:*
{"a":3,"b":1,"c":2}
*Output:*
{"b":1,"c":2,"a":3}
# *7. Remove duplicate values from dictionary*
*Input:*
{"a":10,"b":20,"c":10,"d":30}
*Output:*
{"a":10,"b":20,"d":30}
# *8. Create dict of number → square*
*Input:*
n = 5
*Output:*
{1:1, 2:4, 3:9, 4:16, 5:25}
# *9. Check if two dictionaries are equal*
*Input:*
d1 = {"a":1,"b":2}
d2 = {"b":2,"a":1}
*Output:*
Equal
# *10. Count words in a sentence*
*Input:*
"i love python and i love coding"
*Output:*
{"i":2, "love":2, "python":1, "and":1, "coding":1}
# *11. Find common keys in two dictionaries*
*Input:*
d1 = {"a":1,"b":2,"c":3}
d2 = {"b":100,"c":200,"d":300}
*Output:*
["b", "c"]
# *12. Invert a dictionary with list values*
*Input:*
{"a":[1,2], "b":[3,4]}
*Output:*
{1:"a", 2:"a", 3:"b", 4:"b"}
# *13. Remove a key if value is even*
*Input:*
{"a":2, "b":5, "c":8}
*Output:*
{"b":5}
# *14. Find all keys whose value is a list*
*Input:*
{"a":10, "b":[1,2], "c":[5], "d":20}
*Output:*
["b", "c"]
# *15. Group values by length*
*Input:*
["cat","dog","see","apple","ball"]
*Output:*
{
3: ["cat","dog","see"],
5: ["apple"],
4: ["ball"]
}"""