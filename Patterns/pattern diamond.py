def diamond(n):
    n = (n//2) +1
    for i in range(0,n+1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(i*2-1):
            print("*", end="")
        print()
    for i in range(0,n):
        for j in range(i+1):
            print(" ",end="")
        for j in range(n*2-2-i*2-1,0,-1):
            print("*",end="")
        print()

# for i in range(30):
#     diamond(i)
diamond(7)