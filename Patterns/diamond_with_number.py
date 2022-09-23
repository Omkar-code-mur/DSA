def dia_num(n):
    n= n//2+1
    for i in range(n):
        for j in range(n-i):
            print(" ", end="")
        for j in range(i*2-1):
            if i-j <= 0:
                print(abs(j-i+2), end="")
            else:
                print(i-j,end='')
        print()
    for i in range(n,0,-1):
        for j in range(n-i):
            print(" ", end="")
        for j in range(i*2-1):
            if i-j <= 0:
                print(abs(j-i+2), end="")
            else:
                print(i-j,end='')
        print()

dia_num(7)