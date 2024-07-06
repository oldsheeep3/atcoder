
N = int(input())

for i in range(N):
    c = int(input())
    count = cmb(c,6)
    print(count%998244353)