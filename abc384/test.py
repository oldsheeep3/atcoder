A = [0,1,2,3,4,5,6] # N = 7
N = 7
A +=A
for i in range(N):
    for j in range(N-1):
        print(A[i:i+j+1])
        