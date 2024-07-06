N = int(input())
X = [[]]
for i in range(N):
    X.append([])
for i in range(N-1):
    a,b = map(int,input().split())
    X[a].append(b)
print(X)