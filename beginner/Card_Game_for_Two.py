N = int(input())
a = map(int, input().split())
output = 0
b = sorted(a)
for n in range(N):
    output = output + ((-1)**n)*b[n]
print(abs(output))