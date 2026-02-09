#write a python program to find the longest word in a string and print it.
#using for loop and if condition
a="python java javascript"
words=a.split()
longest_word=""
for word in words:
    if len(word)>len(longest_word):
        longest_word=word
print(longest_word)

#using max function
a="python java javascript"
words=a.split()
longest_word=max(words,key=len)
print(longest_word)

#using sorted function
a="python java javascript"
words=a.split()
longest_word=sorted(words,key=len)[-1]
print(longest_word)
