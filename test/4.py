#Q4. Find the Most Frequent Character

#Write a Python program to find the most frequently occurring character in a string.


s = "success"
m = {}
for char in s:
    if char in m:
        m[char] += 1
    else:
        m[char] = 1
r= max(m, key=m.get)
print("Most frequent character:", r)