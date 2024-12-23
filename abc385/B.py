H,W,X,Y = map(int,input().split())
S = [list(input()) for _ in range(H)]
T = list(input())
ans = [X-1,Y-1,0]
def move(now,direction):
    if direction == "U" and now[0] > 0:
        if S[now[0]-1][now[1]] == "#":
            pass
        else:
            now[0] -= 1
            if S[now[0]][now[1]] == "@":
                S[now[0]][now[1]] = "."
                ans[2] += 1
    if direction == "D" and now[0] < H-1:
        if S[now[0]+1][now[1]] == "#":
            pass
        else:
            now[0] += 1
            if S[now[0]][now[1]] == "@":
                S[now[0]][now[1]] = "."
                ans[2] += 1
    if direction == "L" and now[1] > 0:
        if S[now[0]][now[1]-1] == "#":
            pass
        else:
            now[1] -= 1
            if S[now[0]][now[1]] == "@":
                S[now[0]][now[1]] = "."
                ans[2] += 1
    if direction == "R" and now[1] < W-1:
        if S[now[0]][now[1]+1] == "#":
            pass
        else:
            now[1] += 1
            if S[now[0]][now[1]] == "@":
                S[now[0]][now[1]] = "."
                ans[2] += 1
    return now
for i in T:
    ans = move(ans,i)
ans[0] += 1
ans[1] += 1

print(*ans)