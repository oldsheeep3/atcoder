N, Q = map(int, input().split())
# 辞書を使用して各リストを管理
lists = {f"c{i}": [i] for i in range(N + 1)}

for _ in range(Q):
    x, y, z = map(int, input().split())
    if x == 1 and f"c{y}" == f"c{z}":
        # yとzのリストを結合し、重複を排除
        lists[f"c{y}"] = sorted(lists[f"c{y}"] + lists[f"c{z}"], reverse=True)
        # Lの更新を行う
        for key in lists.keys():
            if key == f"c{z}":
                lists[f"c{z}"] = lists[f"c{y}"]
    else:
        # z-1が範囲内か確認
        if z - 1 < len(lists[f"c{y}"]):
            print(lists[f"c{y}"][z - 1])
        else:
            print("-1")
