
def pgm3(s):
    stack = []
    curr = ""
    num = 0
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '[':
            stack.append((curr, num))
            curr, num = "", 0
        elif char == ']':
            prev, num1 = stack.pop()
            curr = prev + (num1 * curr)
        else:
            curr += char
    return curr


if __name__ == "__main__":
    user_input = input("Enter string : ")
    result = pgm3(user_input)
    print(f"Decoded result: {result}")

"""
def pgm2(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


nums = [3,0,1]
result= pgm2(nums)
print(result)



def pgm1(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in s:
        if counts[char] == 1:
            return char
            
    return -1


if __name__ == "__main__":
    s = input("enter a string:")
    result= pgm1(s)
    print(result)
"""

