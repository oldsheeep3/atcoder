N = int(input())
for n in range(7):
    if N < pow(10,3+n):
        print(N//pow(10,n) * pow(10,n))
        break