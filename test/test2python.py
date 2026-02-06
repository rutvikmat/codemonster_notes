"""
#1 Hollow Square Star Pattern
n = 5

for i in range(n):
    if i == 0 or i == n - 1:
        print("* " * n)
    else:
        print("* " + "  " * (n - 2) + "*")

"""
"""
#2 Inverted Number Pattern

num = 4
for i in range(num, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
"""
"""
#3 palindrome
s="Madam"
s=s.lower()
if s==s[::-1]:
    print("Palindrome")
else:    
    print("Not a palindrome")

"""
"""
s = "success"
m = {}
for char in s:
    if char in m:
        m[char] += 1
    else:
        m[char] = 1
r= max(m, key=m.get)
print("Most frequent character:", r)
"""
"""
Q5. Find Second Largest Element in a List



n = [12, 45, 23, 67, 45, 89]

largest = n[0]
s_largest = n[0]

for num in n:
    if num > largest:
        s_largest = largest
        largest = num
    elif num > s_largest and num != largest:
        s_largest = num

print("Second largest number:", s_largest)



numbers = [1, 2, 3, 4, 5]
k = 2

n = len(numbers)
k = k % n 

rotated_list = numbers[-k:] + numbers[:-k]

print(rotated_list)


Dictionary Program (1)
================================
Q7. Get the required output
===========================
Sample Input - 20
output -> {5:25,10:100,15:225,20:400}  
"""
s=int(input("enter Number:"))
d={}
for i in range(5,s+1,5):    
    d[i]=i**2
print(d)

