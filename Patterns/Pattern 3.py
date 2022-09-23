def pattern_3(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if n+i-j >99:
                print(n + i - j, end=' ')
            elif n+i-j>9:
                print(n+i-j, end='  ')
            else:
                print(n+i-j, end='   ')
        print()


for i in range(10):
    pattern_3(i)
    print()