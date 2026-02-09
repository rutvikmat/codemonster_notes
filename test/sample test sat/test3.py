'''
Q.1

n=int(input("enter the number :"))
a=list(map(int,input("enter seq : ").split()))

res = n * a
print(res)
'''
'''
Q.2
input :
2 4 8 14 22 
output :
32
Explanation:
The difference between consecutive numbers is increasing by 2 each time:
4-2=2, 8-4=4, 14-8=6, 22-14=8. Next difference = 10 → 22+10=32.




a= list(map(int , input("Enter sequence :").split()))

dif = a[1] - a[0]
n_dif = dif + 2*(len(a)-1)
print(a[-1] + n_dif)
'''
'''
Q3 – Count Elements Greater Than Average
=========================================
Input:
2 5 6 3 7

Output:
3

Explanation:
Average = (2+5+6+3+7)/5 = 4.6. Count numbers strictly greater than 4.6 → 5, 6, 7 → 3 elements.
Trick: careful with strictly greater, not ≥.



a = list(map(int , input("Enter sequence :").split()))
avg = sum(a)/len(a)
count = 0
for i in a:
    if i > avg:
        count += 1
print(count)

'''
'''
Q4 – Alternating Sum
=====================

Input:
4 5 6 7 8

Output:
6

Explanation:
Calculate sum by alternating adding and subtracting: 4 - 5 + 6 - 7 + 8 = 6.
Tricky because it’s not a regular sum.

a = list(map(int , input("Enter sequence :").split()))
res = 0
for i in range(len(a)):
    if i % 2 == 0:
        res += a[i]
    else:
        res -= a[i]
print(res)

'''
'''
Q5 – Count Elements That Are Equal to Index
============================================
Input:
0 2 3 1 4

Output:
3

Explanation:
Count elements where element value = its index:

Index 0 → 0 ✅
Index 1 → 2 ❌
Index 2 → 3 ❌
Index 3 → 1 ❌
Index 4 → 4 ✅
So count = 2 ✅ (Wait, carefully count: index 0 (0) + index 4 (4) = 2, not 3). Correction → Output = 2


arr = [0, 2, 3, 1, 4]

count = 0
for i in range(len(arr)):
    if arr[i] == i:
        count += 1

print(count)
'''

'''
Q6 – Product Except Self
=========================
Input:
1 2 3 4

Output:
24 12 8 6

Explanation:
Each element in output = product of all other elements:

1 → 2×3×4=24
2 → 1×3×4=12
3 → 1×2×4=8
4 → 1×2×3=6


lst = [1,2,3,4]
res = []
for i in range(len(lst)):
    prod = 1
    for j in range(len(lst)):
        if i != j:
            prod *= lst[j]
    res.append(prod)
print(res)

'''
