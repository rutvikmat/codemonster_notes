'''#pattern programs
for i in range(5):
    print('*', end=' ')


* * * * *
* * * * *
* * * * *

'''
for i in range(5):
    for j in range(i,5):
        print('*', end=' ')
    print()

