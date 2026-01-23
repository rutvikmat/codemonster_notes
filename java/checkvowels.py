s='sachin'
print(s)
lst=['a','e','i','o','u']
vo,co=0,0
for i in s:
    if i in lst:
        vo+=1
    else:
        co+=1
print('vowels',vo)
print('consonants',co)  