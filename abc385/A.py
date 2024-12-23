A,B,C = map(int,input().split())
if A+B == C or B+C == A or C+A == B or A == B == C:
    print("Yes")
else:
    print("No")