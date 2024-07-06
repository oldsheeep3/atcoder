A = []
q = []
Q = int(input())
for n in range(Q):
    q.append(list(map(int,input().split())))

for n in range(Q):
    if q[n][0] == 1:
        A.append(q[n][1])
    else:
        ans = A[len(A)-q[n][1]]
        print(ans)
