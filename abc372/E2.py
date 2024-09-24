N,Q = map(int,input().split())
L = ["c" + str(i) for i in range(N+1)]
for i,j in zip(L,range(N+1)):
    globals()[i] = [j]
for _ in range(Q):
    x,y,z = map(int,input().split())
    if x == 1 and L[y] != L[z]:
            globals()[L[y]] = sorted(globals()[L[y]] + globals()[L[z]],reverse=True)
            L = ",".join(L).replace(L[z], L[y]).split(",")
    elif x == 2:
        try:
            print(globals()[L[y]][z-1])
        except:
            print("-1")