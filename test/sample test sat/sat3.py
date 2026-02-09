#Q.1
n=3
lst =[1,2,3]
res = n * lst
print(res)

#Q.2
lst = [2,4,8,14,22]
diff = lst[1] - lst[0]
n_diff = diff + 2*(len(lst)-1)
print(lst[-1] + n_diff)

#Q.3
lst=[2,5,6,3,7]
avg = sum(lst)/len(lst)
count = 0
for i in lst:
    if i > avg:
        count += 1
print(count)

#Q.4
a=[4,5,6,7,8]
res = 0
for i in range(len(a)):
    if i % 2 == 0:
        res += a[i]
    else:
        res -= a[i]
print(res)

#Q.5
lst = [0, 2, 3, 1, 4]

count = 0
for i in range(len(lst)):
    if lst[i] == i:
        count += 1

print(count)

#q.6
lst = [1,2,3,4]
res = []
for i in range(len(lst)):
    product = 1
    for j in range(len(lst)):
        if i != j:
            product *= lst[j]
    res.append(product)
print(res)