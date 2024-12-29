inp = list(map(int,input().split()))
abcde = list('ABCDE')
lists = {i:j for i,j in zip(abcde,inp)}
for l in range(1,pow(2,5)):
    check = bin(pow(2,6) - l - 1)[3:]
    ok = [j if i == '0' else '' for i,j in zip(list(check),abcde)]
    key = ''
    val = 0
    for k in ok:
        if k != '':
            key += k
            val += lists[k]
    lists[key]=val
# print(lists)
lists = sorted(lists.items())
lists2 = sorted(lists, key=lambda x:x[1], reverse=True)
for i in lists2:
    print(i[0])