N,Q = map(int,input().split())
L = [[] for _ in range(N+1)]
cc = [i in range(N+1)]
for _ in range(Q):
    x,y,z = map(int,input().split())
    if x == 1:
        ss = L[y]+L[z]+[y,z]
        L[y] = list(set(ss))
        L[z] = L[y]
        print(L)
    else:
        try:
            L[y].sort(reverse=True)
            print(L[y][z-1])
        except:
            print("-1")