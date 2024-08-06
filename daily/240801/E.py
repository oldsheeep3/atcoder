N,M = map(int,input().split())
V = [[] for _ in range(N)]
Vc = [0 for _ in range(N)]

def find2(l, x):
    return l.index(x) if x in l else -1

for i in range(M):
    v,u = map(int,input().split())
    V[v-1].append(u)
    V[u-1].append(v)
    Vc[v-1] += 1
    Vc[u-1] += 1
if find2(Vc,0) == -1:
    try:
        n = Vc.index(1)
        a = n + 1
        b = V[n][0]
        V[n].remove(b)
        V[b-1].remove(a)
        for _ in range(M-2):
            a = b
            b = V[a-1][0]
            V[a-1].remove(b)
        z = V[b-1][1]
        print("Yes")
    except:
        print("No")
else:
    print("No")