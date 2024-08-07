def pedir_num(n):
    for p in range(1, n+1):
        print(end= '\n')
        for q in range(1,n+1):
            if p >=q:
                print(p,end='')
    print(end ='\n')


pedir_num(10)