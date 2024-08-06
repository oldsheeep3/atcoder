N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
for i in B:
    try:
        A = A[A.index(i)+1:]
    except:
        print("No")
        break
else:
    print("Yes")