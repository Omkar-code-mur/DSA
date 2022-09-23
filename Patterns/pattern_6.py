def hour_glass(n):
    n=n//2+1
    for i in range(n-1):
        for j in range(i):
            print(" ",end="")
        for j in range(n*2-1-i*2):
            print("*",end="")
        print()
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(i*2-1):
            print("*",end="")
        print()
        
hour_glass(5)