S = list(input())
S = [int(i) for i in S]
before = -11
ans = []
for i in S:
    # print(i,before)
    if i+before == 0:
        # print("-1")
        before = -11
    else:
        before = i
        ans.append(i)
print(len(ans))