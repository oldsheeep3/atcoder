import math
K = int(input())
C = list(map(int,input().split()))
Csum = 0
Cb = 1
for n in range(len(C)):
    Csum = Csum + C[n]
    Cb = Cb * math.factorial(C[n])

ans = int((math.factorial(Csum)/(Cb**K)))%998244353
print(ans)