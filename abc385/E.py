N = int(input())
I = {i+1:[] for i in range(N) }
for _ in range(N-1):
    a,b = map(int,input().split())
    I[a].append(b)
    I[b].append(a)
Ls = {i+1:len(I[i+1]) for i in range(N)}
L = {i+1:len(I[i+1]) for i in range(N)}
print(I)
print(L)