"""
21. **Diagonal Line (Left to Right)**
*      
  *    
    *  
      *


n = 4

for i in range(n):
    print("  " * i + "*")

22. Diagonal Line (Right to Left)**


      *
    *  
  *    
*      


n = 4

for i in range(n):
    print("  " * (n - i - 1) + "*")

23. **Both Diagonals (X Pattern in Square)**

*     *
 *   * 
  * *  
   *   
  * *  
 *   * 
*     *

n = 7

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

24. **Hollow Square with Diagonal**

* * * * *
*   *   *
* *   * *
*   *   *
* * * * *



n = 5

for i in range(n):
    for j in range(n):
        if (
            i == 0 or i == n - 1 or     
            j == 0 or j == n - 1 or     
            i == j or                   
            i + j == n - 1              
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

25. **Border + Cross (Box with +)**

* * * * *
*   *   *
* * * * *
*   *   *
* * * * *
n = 5
mid = n // 2

for i in range(n):
    for j in range(n):
        if (
            i == 0 or i == n - 1 or      
            j == 0 or j == n - 1 or      
            i == mid or                 
            j == mid                    
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
print()

"""
"""
26. **Triangle with Gaps**
n = 5
for i in range(n):
    for j in range(n):
        if j == i  or j == 0 or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

* 
* *
*   *
*     *
* * * * *


27. **Inverted Hollow Triangle**
n = 5
for i in range(n):
    print(' ' * i, end='')
    if i == 0:
        print('* ' * n)  
    elif i == n - 1: 
        print('*') 
    else:
        inner_spaces = 2 * (n - i - 1) - 1
        print('*' + ' ' * inner_spaces + '*')

* * * * *
 *     *
  *   *
   * *
    *


28. **Right-Angle Hollow Triangle**
n = 5
for i in range(n):
    for j in range(n):
        if j == i  or j == 0 or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
*
* *
*   *
*     *
* * * * *

29. **Pyramid with Alternating Rows**
n=6
for i in range(n):
    print(' '*(n-i)+'* '*(i-1))
for i in range(n-2,0,-1):
    print(' '*(n-i)+'* '*(i-1))
   *
  * *
 * * *
* * * *
 * * *
  * *
   *

30. **Number of Stars Same as Row (Upside Down)**
n=5
for i in range(n,-1,-1):
    print('* '* i,end=' ')
    print()

* * * * *
* * * *
* * *
* *
*
"""
#35.Hourglass Hollow Pattern
"""
* * * * *
*       *
*   *   *
*       *
* * * * *

Outer border → always *

Middle row & middle column → *

Else → space



n = 5
mid = n // 2

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or (i == mid and j == mid):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""

#36.Star Spiral (Matrix Style)
"""
(Stars printed in spiral order — advanced logic)

Use 4 boundaries: top, bottom, left, right

Print stars while shrinking boundaries inward

n = 5
matrix = [[" "]*n for _ in range(n)]

top, bottom, left, right = 0, n-1, 0, n-1

while top <= bottom and left <= right:
    for j in range(left, right+1):
        matrix[top][j] = "*"
    top += 1

    for i in range(top, bottom+1):
        matrix[i][right] = "*"
    right -= 1

    if top <= bottom:
        for j in range(right, left-1, -1):
            matrix[bottom][j] = "*"
        bottom -= 1

    if left <= right:
        for i in range(bottom, top-1, -1):
            matrix[i][left] = "*"
        left += 1

for row in matrix:
    print(" ".join(row))

"""

#37.Concentric Squares
"""
* * * * * * *
*           *
*   * * *   *
*   *   *   *
*   * * *   *
*           *
* * * * * * *


n = 7
for i in range(n):
    for j in range(n):
        layer = min(i, j, n-1-i, n-1-j)
        if layer % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""


#38.Chessboard Pattern
"""
*   *   *   *
  *   *   *  
*   *   *   *
  *   *   *  

If (row + col) % 2 == 0 → star


rows, cols = 4, 7

for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""
#39.Star Waves / Zig-Zag
'''
    *       *
  *   *   *   *
*       *       *

Stars placed using fixed column gaps

Row-based offset


rows = 3
cols = 15
positions = [
    [4, 12],
    [2, 6, 10, 14],
    [0, 8, 16]
]

for i in range(rows):
    for j in range(cols):
        if j in positions[i]:
            print("*", end="")
        else:
            print(" ", end="")
    print()

"""
#40.Triangular Spiral
*
* *
*   *
*     *
* * * * *

Left column → stars

Bottom row → stars

Diagonal boundary → star



n = 5

for i in range(n):
    for j in range(i+1):
        if j == 0 or i == n-1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



41. **Diamond Outline Inside Square**

* * * * * * *
*     *     *
*   *   *   *
* *     * * *
*   *   *   *
*     *     *
* * * * * * *

n = 7
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or j == n-i-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''

42. **Concentric Hollow Diamonds**


    *    
   * *   
  *   *  
 *     * 
  *   *  
   * *   
    *


n = 4

for i in range(1, n+1):
    print(' '*(n-i) + '*'  + ' '*(2*i-3) + ('*' if i>1 else ' '))

for i in range(n-1, 0, -1):
    print(' '*(n-i) + '*' + ' '*(2*i-3) + ('*' if i>1 else ' '))
'''
'''
43. **Triangle + Inverted Triangle (Sandwich Pattern)**

*
* *
* * *
* * * *
* * *
* *
*

n = 4

for i in range(1, n+1):
    print('* ' * i)

for i in range(n-1, 0, -1):
    print('* ' * i)
'''
'''
44. **Right-Shifted Pyramid**


        *
      * *
    * * *
  * * * *

n=5
for i in range (n):
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(i):
            print('*',end=' ')
    print()

'''
'''
45. **Star Arrow (Right Arrow)**

*
* *
* * *
* * * *
* * *
* *
*

n = 4

for i in range(1, n+1):
    print('* ' * i)

for i in range(n-1, 0, -1):
    print('* ' * i)

45. **Star Arrow (Right Arrow)**
n = 4
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
''' 
'''
46. **Star Arrow (Left Arrow)**

n = 4
for i in range(1, n + 1):
    for g in range(n - i):    
        print("  ", end="")
    for j in range(i):         
        print("*", end=" ")
    print()
for i in range(n - 1, 0, -1):
    for g in range(n - i):     
        print("  ", end="")
    for j in range(i):         
        print("*", end=" ")
    print()
'''
'''   

47. **Double-Sided Arrow**

n = 3
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
'''
'''
48. **Y Shape**

n = 4
for i in range(n):
    for j in range(2*n - 1):
        if j == i or j == 2*n - 2 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(n - 1):
    for j in range(2*n-1):
        if j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

49. **Star Heart Shape ❤️ (interview favorite for creativity)**


n = 8          # height
width = 9      # columns (odd for symmetry)
mid = width // 2

for i in range(n):
    for j in range(width):
        if (
            # upper heart lobes
            (i < 3 and (
                (j == mid-2-i) or (j == mid+2+i) or
                (i == 1 and (j == mid-1 or j == mid+1)) or
                (i == 2 and (j == mid))
            )) or
            
            # lower inverted triangle
            (i >= 2 and abs(j - mid) <= (n - i - 1))
        ):
            print("*", end="")
        else:
            print(" ", end="")
    print()

#50 - christmas tree
n = 5
for i in range(1, n + 1):
    for s in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(2):
    for j in range(n - 1):
        print(" ", end="")
    print("*")
'''
## 🔹 **Advanced Matrix-style Star Patterns**
'''
51. **Box Spiral (stars in spiral order)**

```
* * * * *
*     * *
* * * * *
* *      
* * * * *
```
'''



'''
52. **Star Snake (Zig-Zag in matrix)**

```
* * * *
      *
* * * *
*      
* * * *
```
'''
'''
r = 5
c = 4

for i in range(r):
    if i % 2 == 0:
        print('* ' * c)
    else:
        if (i // 2) % 2 == 0:
            print(' ' * (2 * (c - 1)) + '*')
        else:
            print('*')
'''
'''
53. **Hollow Cross inside Square**

```
* * * * * * *
*     *     *
*     *     *
* * * * * * *
*     *     *
*     *     *
* * * * * * *
```
'''
'''
n = 7
mid = n // 2

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*', end=' ')
        elif i == mid or j == mid:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''

'''
54. **Rhombus (Shifted Square)**

```
    * * * * *
   * * * * *
  * * * * *
 * * * * *
* * * * *
```
'''
'''
n=int(input('enter the number'))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(n):
        print('*',end=' ')
    print()
 '''   
'''
55. **Parallelogram**

```
    * * * * *
   * * * * *
  * * * * *
 * * * * *
* * * * *
```

'''
'''
n=int(input('enter the number'))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(n):
        print('*',end=' ')
    print()
 '''

n = 5                 # rows
width = 9             # columns (odd)
mid_row = n // 2
mid_col = width // 2

for i in range(n):
    for j in range(width):
        if (
            j == 2 * i or                    # left diagonal
            j == width - 1 - 2 * i or        # right diagonal
            i == mid_row                    # middle row
        ):
            print("*", end="")
        else:
            print(" ", end="")
    print()
