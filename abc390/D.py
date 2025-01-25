def in1(type=int):
    if type == int:
        return int(input())
    return input()
def ins(type=int):
    if type == int:
        return map(int,input().split())
    return map(str,input().split())
def inl(type=int):
    if type==int:
        return list(map(int,input().split()))
    return list(map(str,input().split()))
def inll(n,type=int):
    if type==int:
        return [list(map(int,input().split())) for _ in range(n)]
    return [list(map(str,input().split())) for _ in range(n)]
def yes():
    print('Yes')
def no():
    print('No')

N = in1()
A = inl()
c = []
# for k in range(N):
#     temp = [0]
#     for i,j in zip(A,bin(pow(2,len(bin(N)[2:])+1)+k)[3:]):
#         if j == "1":
#             temp[0] += i
#         else:
#             temp.append(i)
#     temp.sort()
#     if temp not in c:
#         c.append(temp)

def back(lst):
    le = len(lst)
    if le < 2:
        return []  # le < 2 の場合は空のリストを返す
    anss = []  # anss をここで初期化
    for i in range(le - 1):
        for j in range(i + 1, le):
            new_lst = lst[:i] + lst[i + 1:]  # lst の i 番目の要素を除外
            new_lst[j - 1] += lst[i]  # j 番目の要素に i 番目の要素を加える
            anss.append(new_lst)  # 修正したリストを anss に追加
            anss += back(new_lst)  # 再帰的に呼び出し
    return anss


def remove_duplicates_2d(lst):
    seen = set()
    unique_list = []
    
    for sublist in lst:

        sublist_tuple = tuple(sublist)
        if sublist_tuple not in seen:
            seen.add(sublist_tuple)
            unique_list.append(sublist)

    return unique_list
ans = []
# print(back(A))
# print(remove_duplicates_2d(back(A)))
for i in remove_duplicates_2d(back(A)):
    temp = 0
    for j in i:
        temp ^= j
    if temp not in ans:
        ans.append(temp)
print(len(ans)+1)