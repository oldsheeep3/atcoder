N,K = map(int,input().split())
A = list(map(int,input().split()))
s = sum(A)
a = sorted(A)
if K <= 0 and s < K:
    print("No")
else:
    print("Yes")
    print(*a)