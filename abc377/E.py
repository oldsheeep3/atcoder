N,K = map(int,input().split())
P = list(map(int,input().split()))

def cycle(start):
    visited = {}
    cur = start
    count = 0
    his = []

    while True:
        if cur in visited:
            return his
        visited[cur] = count
        his.append(cur)
        cur = P[cur] - 1
        count += 1
cyc = {i: i for i in range(K)}
for i in range(N):
    if i not in cyc:
        c = cycle(i)
        for j in c:
            cyc[j] = c
print(cyc)