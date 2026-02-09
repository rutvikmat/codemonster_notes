#using slicing
a="madam"
if a==a[::-1]:
    print("palindrome")
else:    
    print("not palindrome")

#using for loop
a="madam"
reverse=""
for char in a:
    reverse=char+reverse
if a==reverse:
    print("palindrome")
else:
    print("not palindrome")

#using while loop
a="madam"
reverse=""
i=len(a)-1
while i>=0:
    reverse+=a[i]
    i-=1
if a==reverse:
    print("palindrome")
else:
    print("not palindrome")

#using recursion
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

a="madam"
if is_palindrome(a):
    print("palindrome")
else:    
    print("not palindrome") 


