M = int(input())
n = [(pow(3,10-i),10-i) for i in range(11)]
ans = []
for a,b in n:
    c = M//a
    for _ in range(c):
        ans.append(b)
    M = M - a*c
    
print(len(ans))
print(*ans)