from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def count_unique_combinations(ranges):
    total_combinations = 0
    overlap_counts = {}

    # 各範囲の組み合わせを計算
    for start, end in ranges:
        length = end - start + 1
        if length >= 2:
            total_combinations += cmb(length, 2)  # nC2 を計算

        # 範囲をキーとしてオーバーラップをカウント
        for i in range(start, end + 1):
            if i not in overlap_counts:
                overlap_counts[i] = 0
            overlap_counts[i] += 1

    # 重複を引く部分
    total_overlaps = 0
    for count in overlap_counts.values():
        if count > 1:  # 2つ以上の範囲に含まれる場合
            total_overlaps += cmb(count, 2)  # その重複の組み合わせを計算

    # 重複を引く
    total_combinations -= total_overlaps

    return total_combinations




N,M = map(int,input().split())
LR = [list(map(int,input().split())) for _ in range(N)]
LR.sort()
lasti = [0,0]
histM = []
histL = []
xx = []

maxa = 0
mina = 200000
for i in LR:
    if i[0] != lasti[0]:
        histM.append(i)
        if lasti not in histM:
            histL.append(lasti)
        if lasti[1] < i[0] and lasti != [0,0]:
            xx.append([lasti[1],i[0]])
    lasti=i
histL.append([M,M])

result = count_unique_combinations(LR)



print(histM)
print("ユニークな組み合わせの数:", result)
print(histL)
print(xx)