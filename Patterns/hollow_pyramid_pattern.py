def hollow_pyrsmid(n):
    for i in range(n):
        for j in range(n-i):
            print(" ",end="")
        print("*",end="")
        if i == 0:
            print()
            continue
        for j in range(i*2-1):
            print(" ",end="")
        print("*",end="")
        print()
    
    for i in range(n*2+1):
        print("#",end="")

hollow_pyrsmid(5)