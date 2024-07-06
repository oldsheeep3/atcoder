import itertools
K = int(input())
C = list(map(int,input().split()))
Csum = 0
C1=[]
for n in range(len(C)):
    Csum = Csum + C[n]
    if C[n] != 0:
        C1.append(C[n])
C2=[]
for n in range(len(C1)):
    for m in range(C1[n]):
        C2.append(n)
a = 0
for n in range(K):
    a = a + len(set(list(itertools.permutations(C2,K-n))))


print(a%998244353)