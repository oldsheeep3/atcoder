S = input()
c = ["A","B","C"]
ans = "Yes"
for i in c:
    if i not in S:
        ans = "No"
        break
print(ans)
