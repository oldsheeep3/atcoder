N,M,K = map(int,input().split())
X = []
o = []
x = []
for m in range(M):
    X.append(list(map(int,input().split())))

for m in range(M):
    if X[m][X[m][1]+1] == "o":
        o.append(X[m])
    else:
        x.append(X[m])
