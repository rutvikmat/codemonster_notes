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