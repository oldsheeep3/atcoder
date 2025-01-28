import sys
sys.setrecursionlimit(10000000) 



H,W,N = map(int,input().split())
coins = [[0 for _ in range(H)] for _ in range(W)]

for i in range(N):
    x,y = map(int,input().split())
    coins[x][y] = 1
print(coins)

def dfs(x, y, total_coins):
    if x < 0 or x >= len(coins) or y < 0 or y >= len(coins[0]):
        return total_coins
    
    if coins[x][y] == 1:
        total_coins += 1
        coins[x][y] = 0
    
    # 右か下に移動
    right_coins = dfs(x, y+1, total_coins)
    down_coins = dfs(x+1, y, total_coins)
    
    return max(right_coins, down_coins)

# 実行
result = dfs(0, 0, 0)
print(result)