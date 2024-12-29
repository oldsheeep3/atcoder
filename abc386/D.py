N,M = map(int,input().split())
XYC = [[int(i) if j <= 1 else i for i,j in zip(list(map(str,input().split())),range(3))] for _ in range(M)]
# print(XYC)
XYC = sorted(XYC,reverse=True)
# print(XYC)
black = [-1]
white = [N+1]
for i in XYC:
    if i[2] == 'B':
        black.append(i[1])
        white.append(-1)
    else:
        black.append(black[-1])
        white.append(i[1])
# print(black[1:])
# print(white[1:])

for i in range(M):
    a = black[M-i]
    white[M-i] = white[M-i] if white[M-i] != -1 else N+1 if i<1 else white[M-i+1]
    b = white[M-i]
    if a >= b:
        print('No')
        break
else:
    print('Yes')