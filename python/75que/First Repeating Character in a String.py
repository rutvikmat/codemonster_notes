#First Repeating Character in a String
#using for loop

ip="abacbd"
for char in ip:
    if ip.count(char) > 1:
        print(char)
        break

