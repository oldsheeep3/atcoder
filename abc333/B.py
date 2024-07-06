A = []
A.append(input())
A.append(input())
B = [1,1]
for n in range(2):
    for m in range(2):
        if A[n][m] == "A":
            if A[n][(m+1)%2] == "D" or A[n][(m+1)%2] == "C":
                B[n] = 2
                break     
        elif A[n][m] == "B":
            if A[n][(m+1)%2] == "D" or A[n][(m+1)%2] == "E":
                B[n] = 2
                break
        elif A[n][m] == "E":
            if A[n][(m+1)%2] == "B" or A[n][(m+1)%2] == "C":
                B[n] = 2
                break
if B[0] == B[1]:
    print("Yes")
else:
    print("No")