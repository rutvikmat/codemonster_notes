# Count the number of occurrences of a character in a string
a="success"
char='s'
count=0
for c in a:
    if c==char:
        count+=1
print(count)

#using list comprehension
a="success"
char='s'
count=sum(1 for c in a if c==char)
print(count)

#using count method
a="success"
char='s'
count=a.count(char)
print(count)
