N = int(input())
L,R = -1,-1
l,r = 0,0
for i in range(N):
    a,s = map(str,input().split())
    a = int(a)
    if s == "L":
        if L != -1:
            l += abs(L-a)
        L = a
    else:
        if R != -1:
            r += abs(R-a)
        R = a
print(l+r)