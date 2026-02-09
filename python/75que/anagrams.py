# Check if the two strings "listen" and "silent" are anagrams of each other.
#using sorted function
a1="listen"
a2="silent"
if sorted(a1)==sorted(a2):
    print("anagram")
else:
    print("not anagram")

#using for loop and if condition
a1="listen"
a2="silent"
if len(a1)!=len(a2):
    print("not anagram")
else:
    for char in a1:
        if char not in a2:
            print("not anagram")
            break
    else:
        print("anagram")

#using list comprehension
a1="listen"
a2="silent"
if len(a1)!=len(a2):
    print("not anagram")
else:
    if all(char in a2 for char in a1):
        print("anagram")
    else:
        print("not anagram")

#using dictionary
a1="listen"
a2="silent"
dict1={}
dict2={}
for char in a1:
    dict1[char]=dict1.get(char,0)+1
for char in a2:
    dict2[char]=dict2.get(char,0)+1
if dict1==dict2:
    print("anagram")
else:
    print("not anagram")
