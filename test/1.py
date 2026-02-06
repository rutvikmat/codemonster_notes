#Q1. Hollow Square Star Pattern
#Write a Python program to print a hollow square pattern of stars for a given number `n`.

n=5
for i in range(n):
    if i == 0 or i == n - 1:
        print("* " * n)
    else:
        print("* " + "  " * (n - 2) + "*")
