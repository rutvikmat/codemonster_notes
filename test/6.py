#Q6. Rotate a List by K Positions

#Write a Python program to rotate a list to the right by `k` positions.
lst = [1, 2, 3, 4, 5]
k = 2

n = len(lst)
k = k % n 
rotate = lst[-k:] + lst[:-k]
print(lst)
print(rotate)
