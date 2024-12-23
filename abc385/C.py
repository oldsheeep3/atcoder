from itertools import combinations

N = int(input())
H = list(map(int,input().split()))
Tower = {}

for i in range(N):
    if H[i] not in Tower:
        Tower[H[i]]=[]
    Tower[H[i]].append(i)

def count(list):
    if len(list) < 2:
        return len(list)
    dif = list[1]-list[0]
    count = 2
    for i in range(1,len(list)-1):
        if list[i + 1] - list[i] == dif:
            count += 1
    return count if count > 1 else 0

def allList(list):
    ans = 1
    for i in range(len(list)-1):
        for combo in combinations(list, len(list)-i):
            ans = max(count(combo),ans)
            if len(combo) <= ans:
                return(ans)
    return(ans)

def base_n(num_10,n):
    str_n = []
    if num_10 == 0:
        return [0]
    if n == 1 or n == 10:
        return list(str(num_10))
    while num_10:
        str_n.append(num_10%n)
        num_10 //= n
    return str_n[::-1]

def Sbase_n(num_10,n):
    return num_10%n

Tower = dict(sorted(Tower.items(), key=lambda item: len(item[1]), reverse=True))
print(Tower)


ans = 0
L0 = list(Tower.values())[0]
diffL = []
for i in range(len(L0)):
    for j in range(i+1, len(L0)):
        diff = L0[j] - L0[i]
        if diff not in diffL:
            diffL.append(diff)
            # print("-----------------")
            # print(i,j)
            # print(L0[i],L0[j])
            # print(diff)
            print([base_n(k,diff) for k in L0])
            # print([Sbase_n(k,diff) for k in L0])

# LENG = len(L0)
# # print(L0)
# diff = L0[1]-L0[0]
# print(L0)
# L0 = [base_n(i,diff) for i in L0[2:]]
# print(diff)
# print(L0)
# for i in range(len(L0)):
#     for j in range(i+1, len(L0)):
#         print(L0[i],L0[j])

# for i in list(Tower.values()):
#     arr = []
#     if len(i) <= ans:
#         break
#     ans = max(allList(i),ans)
# print(ans)

# [0, 9, 15, 17, 24, 25, 27]