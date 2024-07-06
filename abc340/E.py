N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
hand = 0
for i in range(M):
    bi = B[i]
    hand = A[bi]
    A[bi] = 0
    for n in range(N):
        hands = int((hand-n)/N)
        A[(bi+n+1)%N] += hands
x = ""
for n in range(N):
    x = x + " " + str(A[n])
x = x[1:]
print(x)