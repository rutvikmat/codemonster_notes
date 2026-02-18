ip = "abacbd"

for i in range(len(ip)):
    if ip[i] in ip[:i]:
        print(ip[i])
        break
