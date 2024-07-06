N = int(input())
S = input()
l = -1
m = -1
for i in range(N):
    if S[i] == "|" and l != -1:
        m = int(i)
    elif S[i] == "|" and l == -1:
        l = int(i)
    if S[i] == "*":
        if l != -1 and m == -1:
            print("in")
            break
        else:
            print("out")
            break