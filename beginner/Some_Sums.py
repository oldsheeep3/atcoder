N,A,B = map(int, input().split())
sumB = 0
for n in range(N):
    sumA = 0
    for m in range(len(str(n+1))):
        sumA = int(float((n+1)/(10**m))%10) + sumA
    if sumA >= A and sumA <= B:
        sumB = sumB + n+1
print(sumB)
    