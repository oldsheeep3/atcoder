N,K = map(int,input().split())
A = list(map(int,input().split()))
k = int(K)
A.sort()
B = []
for n in range(len(A)-1):
    B.append(A[n+1]-A[n])
i = 0
m = 0
while k > 0:
    if len(B)-i-1 <= 0:
        for n in range(k):
            if m == 1:
                del B[len(B)-1]
                del A[len(A)-1]
            elif B[0] < B[1]:
                del B[0]
                del A[0]
                m = 0
            elif B[0] > B[1]:
                del B[0]
                del A[0]
                m = 1
        if len(A) != N-K:
            B.append(B[0]*(N-K-len(A)))
        break
    elif B[i] < B[len(B)-1-i]:
        del B[len(B)-1]
        del A[len(A)-1]
        k-=1
        i = 0
    elif B[i] > B[len(B)-1-i]:
        del B[0]
        del A[0]
        k-=1
        i = 0
    else:
        i += 1
print(sum(B))
