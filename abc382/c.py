import bisect
N,M = map(int,input().split())
Ai = list(map(int,input().split()))
B = list(map(int,input().split()))
As = [(Ai[i], i + 1) for i in range(N)]
As = sorted(As, key=lambda x : x[0])
# print(As)
for i in range(1,N):
    if As[i][1] >= As[i-1][1]:
        As[i] = (As[i][0],As[i-1][1])
# print(As)
mA = As[0][0]
for b in B:
    if b < mA:
        print('-1')
    else:
        idx = bisect.bisect_left(As, (b, float('inf'))) - 1
        # print("a:"+str(idx))
        if N > idx >= 0:
            print(As[idx][1])
        else:
            print('-1')