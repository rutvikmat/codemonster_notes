#what is the frequency of each character in the string "mississippi"?
#using
a="mississippi"
freq={}
for char in a:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)


