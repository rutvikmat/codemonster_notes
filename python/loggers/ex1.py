def fun():
    try:
        print('fun is called')
        a=int(input('enter the num1'))
        b=int(input('enter the num2'))
        return a/b
    
    except:
        print('exception is handled..!')
        print('some problem occurred..!')

if __name__ == '__main__':
    print('main() is called')
    res=fun()
    print(f'res {res}')
