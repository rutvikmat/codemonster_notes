#WAP to display index, character and negative index of characters in a string using while loop
'''
r='rutvik'
i=0
n=len(r)
while i<n:
    print(i,r[i],i-n)
    i+=1

#WAP to count number of even and odd numbers using while loop
#ip-> lst=[4,6,3,8,23,72,81]
#even->4
#odd->3
lst=[4,6,3,8,23,72,81]
i=0
even=0
odd=0
n=len(lst)
while i<n:
    if lst[i]%2==0:
        even+=1
    else:
        odd+=1
    i+=1
print("even =",even)
print("odd =",odd)  
'''
#wap to print number of vowels and consonants in a string using while loop
r='rutvik'
i=0
vowel=0
consonant=0
n=len(r)
while i<n:
    if r[i] in 'aeiouAEIOU':
        vowel+=1
    else:
        consonant+=1
    i+=1
print("vowel =",vowel)
print("consonant =",consonant)