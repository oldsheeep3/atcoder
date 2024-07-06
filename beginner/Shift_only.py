N = int(input())
A = list(map(int, input().split()))
B = A
M = 0
a = 1
while a == 1:
    for n in range(len(B)):
        if B[n]%2 == 0:
            B[n] = B[n]/2
        else:
            a = 0
            print(M)
            break
    M = M+1