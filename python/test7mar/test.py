'''
Q1.words.txt contains only lowercase characters and space ' ' characters.
Each word must consist of lowercase characters only.
Words are separated by one or more whitespace characters.

Example:
Assume that words.txt has the following content:

the day is sunny the the
the sunny is is
Your script should output the following, sorted by descending frequency:

the 4
is 3
sunny 2
day 1

'''
with open("words.txt", "r") as r:
    words = r.read().split()


counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1


for word in counts:
    print(word, counts[word])
'''



Q2.
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is 
that adjacent houses have security systems connected and it will automatically contact the police if two adjacent 
houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

 
Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


def rob(nums):
    old = 0
    now = 0

    for n in nums:
        temp = max(now, old + n)
        old = now
        now = temp

    return now


print(rob([1,2,3,1]))      
print(rob([2,7,9,3,1]))    




Q3.
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 


def checkprime(n):
    if n < 2: 
        return 0
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, n):
        if is_prime[i]:
            for multiple in range(i * 2, n, i):
                is_prime[multiple] = False
                
  
    return sum(is_prime)

print(checkprime(16)) 



Q4.
Problem: Custom Sorting Based on Set Bits
You are given a list of integers. Your task is to sort the numbers based on the number of set bits (1s) in their binary representation.
Sorting Rules
Numbers should be sorted in ascending order of the count of set bits in their binary representation.
If two numbers have the same number of set bits, then sort them numerically in ascending order.

Explanation
The set bits of a number refer to the number of 1s in its binary form.

For example:

Number	Binary Representation	Set Bits
5	101	2
3	011	2
7	111	3
10	1010	2

Sorting by the rules:

First compare by set bit count

If counts are equal, compare by number value

Sample Input
[5, 3, 7, 10]
Sample Output
[3, 5, 10, 7]

Explanation of Sample Output

Count the set bits:

5  -> 101  -> 2 bits
3  -> 011  -> 2 bits
7  -> 111  -> 3 bits
10 -> 1010 -> 2 bits

Numbers with 2 set bits → 5, 3, 10

Numbers with 3 set bits → 7

Sort numbers with same set bits:

3, 5, 10

Final sorted list:

[3, 5, 10, 7]

def setbit(n):
    count = 0
    while n > 0:
        count += n % 2
        n //= 2
    return count

nums = [5, 3, 7, 10]
nums.sort(key=lambda x: (setbit(x), x))
print(nums)




Q5.
Longest Word in a Sentence
Problem Statement

Given a sentence, find the longest word in it.

Sample Input
"Python programming is powerful"
Sample Output
"programming"
Explanation

Among all words, programming has the maximum length.


def longest_word(sentence):
    words = sentence.split()
    longest = ""
    
    for word in words:
        if len(word) > len(longest):
            longest = word
            
    return longest

sentence = "Python programming is powerful"
print(longest_word(sentence)) 
'''