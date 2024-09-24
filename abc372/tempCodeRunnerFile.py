N,Q = map(int,input().split())
L = ["c" + str(i) for i in range(N+1)]
for i in L:
    globals()[i] = []
for _ in range(Q):
    x,y,z = map(int,input().split())
    if x == 1:
        globals()[L[y]] = sorted(list(set(globals()[L[y]] + globals()[L[z]] + [y,z])),reverse=True)
        L = ",".join(L).replace(L[z], L[y]).split(",")
    else:
        try:
            print(globals()[L[y]][z-1])
        except:
            print("-1")