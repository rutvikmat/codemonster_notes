#Q2. Inverted Number Pyramid

#Write a Python program to print the following pattern.

num = 4
for i in range(num, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()