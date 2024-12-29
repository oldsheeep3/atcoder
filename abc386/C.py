K = int(input())
S = input()
T = input()

s = len(S)
t = len(T)
if s == t:
    aa = [0 if i==j else 1 for i,j in zip(list(S),list(T))]
    if sum(aa) <= 1:
        print('Yes')
    else:
        print('No')
elif abs(s-t) <= 1:
    if s < t:
        min = s
        Min = S
        max = t
        Max = T
    else:
        min = t
        Min = T
        max = s
        Max = S
    ok = True
    for i in range(min):
        # print("minmax",Min[i],Max[i])
        if Min[i] != Max[i]:
            if Min[i:] != Max[i+1:]:
                # print(Min[i:],Max[i+1:])
                ok = False
            break
    if ok:
        print('Yes')
    else:
        print('No')
else:
    print('No')