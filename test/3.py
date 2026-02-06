#Q3. Check Whether a String is a Palindrome

#Write a Python program to check whether a given string is a palindrome (ignore case).
s="Madam"
s=s.lower()
if s==s[::-1]:
    print("Palindrome")
else:    
    print("Not a palindrome")