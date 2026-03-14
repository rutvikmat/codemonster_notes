
#1. Maximum Subarray Sum 
#Find the maximum sum of a contiguous subarray.
"""

Input
9
-2 1 -3 4 -1 2 1 -5 4

Output
6

n = int(input("Enter range of array:"))
#a = [-2 ,1, -3, 4, -1, 2, 1, -5, 4]
a = list(map(int, input().split()))
current = max_sum = a[0]

for x in a[1:]:
    current = max(x, current + x)
    max_sum = max(max_sum, current)

print("sum of contiguous subarray",max_sum)
"""



#2. Find peak element
#find element greterthan its neigbour

'''

Input
5

1 2 3 1 5

Output
3

n = int(input())
#arr=[1,2,3,1,5]
arr = list(map(int, input().split()))

for i in range(n):
    if (i == 0 or arr[i] > arr[i-1]):
        if (i == n-1 or arr[i] > arr[i+1]):
            print(arr[i])
            break
'''          

'''
#3. Spiral Matrix Traversal
#Print matrix elements in spiral order.

Input
3 3
1 2 3
4 5 6
7 8 9

Output
1 2 3 6 9 8 7 4 5
'''
#4. Count Palindromic Substrings
#Count how many substrings of a string are palindromes.
"""


Input
aaa
Output
6
Explanation

Palindromes:

a, a, a, aa, aa, aaa


p = input("Enter substring of a string: ")
count = 0

for i in range(len(p)):
    for j in range(i, len(p)):
        sub = p[i:j+1]
        if sub == sub[::-1]:
            count += 1

print(count)
"""


#5 kth largest number
#Find the kth largest element in an array.

"""

Input
6
3 2 1 5 6 4
2
Output
5

n = int(input())
arr = list(map(int,input().split()))
k= int(input())
arr.sort(reverse=True)
print(arr[k-1])
"""