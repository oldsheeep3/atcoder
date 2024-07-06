N = int(input())
S = input()
c = 1
ans = 1
for i in range(N-1):
    if S[i] != S[i+1]:
        c += 1
    else:
        ans *= (c+1)//2
        c = 1
ans *= (c+1)//2
print(ans%(pow(10,9)+7))