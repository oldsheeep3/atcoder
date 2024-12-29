N,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
w = len(bin(max(A))[2:])
z = pow(2,w)    
a = [bin(z+i)[3:] if i < pow(2,z-1) else None for i in A]
check = {i:{} for i in range(w)}

for i in range(w):
    [i for i in check[i].items() if i[1] == 1]

for i in range(N):
    for j,k in zip(list(a[i]),range(w)):
        check[k][i] = int(j)

print(check)

def listPrint(a):
    for i in a:
        print(i)

listPrint(a)

# 和が偶数=0 和が奇数=1