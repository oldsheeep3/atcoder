N = int(input())
Nbox = []
for n in range(N-1):
    Narr = list(map(int,input().split()))
    Nbox.append(Narr)

for n in range(N-1):
    A = Narr[n][0]
    B = Narr[n][1]
    n = Narr[n][2]
    