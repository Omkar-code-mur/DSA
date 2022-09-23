def pattern(n):
    cap = 65+n
    lower = 97+n
    for i in range(n):
        for j in range(1, n+1):
            if i % 2 == 0:
                print(chr(cap + i-j), end="")
            else:

                print(chr(lower + i - j), end='')
        print()
    return "\n"


for i in range(10):
    print(pattern(i))