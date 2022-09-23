def diamond(n):
    n = n//2+1
    for i in range(n):
        for j in range(n-i):
            print(' ', end='')
        for k in range(i):
            print('* ', end='')
        print()
    for i in range(n):
        for j in range(i):
            print(" ", end='')
        for k in range(n-i):
            print('* ', end='')
        print()

# for i in range(20):
#     diamond(i)
diamond(7)
# MADE BY PB
