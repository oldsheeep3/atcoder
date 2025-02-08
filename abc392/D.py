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
K = inll(N)

def intIndex(lst,len=False,dict=True):
    index_dict = {}
    index_len = {}
    for index, value in enumerate(lst):
        if value not in index_dict:
            index_dict[value] = 1
        else:
            index_dict[value] += 1
    if len and dict:
        return(index_dict,[len(i) for i in index_dict])
    if len:
        return [len(i) for i in index_dict]
    return index_dict

anss = 0
for i in range(N-1):
    for j in range(i+1,N):
        ans = 0
        A = K[i][1:]
        B = K[j][1:]
        AandB = set(A) & set(B)
        Ac = intIndex(K[i][1:])
        Bc = intIndex(K[j][1:])
        # print(A,B)
        print(AandB)
        for k in AandB:
            ans += Ac[k]*Bc[k]
        anss = max(ans/(K[i][0]*K[j][0]),anss)

print(anss)