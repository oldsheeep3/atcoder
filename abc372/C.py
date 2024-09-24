N,Q = map(int,input().split())
S = list(input())
countabc = 0


def abc(x):
    for i in range(max(0,x-2), min(N-2, x+1)):
        if S[i:i+3] == ['A', 'B', 'C']:
            return(True)
        else:
            return(False)


for i in range(N - 2):
    if S[i:i + 3] == ['A', 'B', 'C']:
        countabc += 1

for _ in range(Q):
    X,C = input().split()
    X = int(X) -1

    if abc(X):
        countabc -= 1
    S[X] = C
    if abc(X):
        countabc += 1
    print(countabc)

