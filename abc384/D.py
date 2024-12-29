N,S = map(int,input().split())
A = list(map(int,input().split()))
sumA = sum(A)
minA = min(A)
check = 0
if min(A) > S:
    print('No')
else:
    if S/sumA >= 1:
        S = S%sumA
        if S == 0:
            print('Yes')
        else:
            for i in range(N+1):
                if check == -1:
                    break
                else:
                    for j in range(N-i):
                        cc = (sum(A[N-i:]) + sum(A[:j])) if i+j else 0
                        if S == cc:
                            print('Yes')
                            check = -1
                            break
                        elif cc > S:
                            print("cc break")
                            break
                        else:
                            continue
            else:
                print('No')
    else:
        for i in range(N):
            for j in range(N-1):
                if S == sum(A[i:i+j+1]):
                    print('Yes')
                    break
                else:
                    continue
            else:
                continue
            break
        else:
            print('No')
