N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(B)
c = 0
d = 0
for i in range(N):
    if A[i] == B[i]:
        c += 1
    else:
        for j in range(N):
            if A[i] == B[j]:
                d += 1
print(c)
print(d)