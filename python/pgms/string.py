#quote mechanism
"""s= 'this is a \'single\' string'
print(s)"""

"""
s=input('enter some name ')

x=0
for i in s:
	print('The char present in +ve index {} and -ve index {} is {}'.format(x,x-len(s),i))
	x=x+1"""

'''s = "B4A1D3"

letters = []
digits = []

for ch in s:
    if ch.isalpha():
        letters.append(ch)
    elif ch.isdigit():
        digits.append(ch)

letters.sort()
digits.sort()

result = "".join(letters) + "".join(digits)
print("Output:", result)'''

"""s = 'a4b3c2'

result = []

i = 0
while i < len(s):
    ch = s[i]
    num = int(s[i + 1])
    result.append(ch * num)
    i += 2

print("Output:", "".join(result))"""

print('a'*4,'b'*3,'c'*2)
s='a4b3c2'
print(s)
res=''
for i in s:
    if i.isalpha():
        ch=i
    else:
        res+=ch*int(i)
print(res)