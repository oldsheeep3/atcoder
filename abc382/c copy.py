import bisect

N,M = map(int,input().split())
Ai = list(map(int,input().split()))
B = list(map(int,input().split()))
A = [(Ai[i],i+1) for i in range(N)]

A = sorted(A, key=lambda x: x[0])
mA = A[0][0]
print(A)
print(B)
for b in B:
    if b < mA:
        print('-1')
    else:
        idx = bisect.bisect_right([x[0] for x in A], b)
        print('idx;'+str(idx))
        if 0 <= idx :
            print(A[idx][1])
        else:
            print('-1')

#     else:
        # idx = bisect.bisect_left([x[0] for x in A], b)
        # print('idx;'+str(idx))
        # if 0 <= idx :
            # print(A[idx][1])
        # else:
            # print('-1')