N = int(input())
A = list(map(int,input().split()))
B = []
A.sort()
for n in A:
    if len(n)>= 8:
        B.append(n)
for n in B:
    