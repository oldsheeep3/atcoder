N = int(input())
H = list(map(int,input().split()))
m = -1
for n in range(N-1):
    if H[n+1] > H[0]:
        m = int(n+2)
        break
print(m)