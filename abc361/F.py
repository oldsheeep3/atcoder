N = int(input())
a = 1
b = 2
c = 0
cc = 0
ans = [1]
while pow(b,2) <= N:
    b = 2
    a += 1
    while cc <= N:
        cc = pow(a,b)
        b+=1
        ans.append(cc)
print(ans)
print(len(ans))