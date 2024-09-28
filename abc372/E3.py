# import heapq

N, Q = map(int,input().split())
lists = {f"c{i}": [i] for i in range(N + 1)}

for i in range(1, Q + 1):
    x, y, z = map(int,input().split())
    if x == 1 and y != z:
        # リストをマージ
        lists[f"c{y}"].extend(lists[f"c{z}"])
        # マージ後にソート
        lists[f"c{y}"].sort(reverse=True)
        # c[z]を削除
        del lists[f"c{z}"]
    elif x == 2:
        # z-1番目の要素を取得
        if f"c{y}" in lists and z - 1 < len(lists[f"c{y}"]):
            print(lists[f"c{y}"][z - 1])
        else:
            print("-1")
