S = list(input());cross={'[':']',']':'','<':'>','>':'','(':')',')':''};tmp=''
for i in S:
 if len(tmp)!=0 and cross[tmp[-1]]==i:tmp=tmp[:-1]
 else:tmp+=i
if len(tmp)==0:print('Yes')
else:print('No')