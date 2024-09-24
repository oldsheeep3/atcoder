N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]
C = []

AB.sort()

print(AB)
for i in range(N-1):
    if AB[i][1] > AB[i+1][1]:
        C.append(AB[i])
        AB.remove(AB[i])

for i in range(len(AB)-1):
    print(str(*AB[i]) + str(*AB[i+1]))

try:
    print(C[0])
    for i in range(len(C)-1):
        print(str(*C[i+1]) + str(*C[i+2]))
except:
    pass