def is_palindrome(s):
    return s == s[::-1]

string = "MOM"

if is_palindrome(string):
    print("Palindrome")
else:
    print("Not Palindrome")