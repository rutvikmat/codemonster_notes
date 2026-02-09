# Non-Repeating Character in a String
#using for loop 
ip = "aabbccde"
char=""
for char in ip:
    if ip.index(char) == ip.rindex(char):
        print(char)
        break

#using list comprehension 
ip = "aabbccde"
result = [char for char in ip if ip.count(char) == 1]
print(result[0])


#using dict
ip = "aabbccde"
freq = {}

for char in ip:
    freq[char] = freq.get(char, 0) + 1

for char in ip:
    if freq[char] == 1:
        print(char)
        break


#using count 
ip = "aabbccde"

for char in ip:
    if ip.count(char) == 1:
        print(char)
        break
