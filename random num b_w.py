
import random as r
ls=[]
i=1
while i < 50:
    ls.append(i*(r.random())+1)
    i+=1
# print(ls)
for ind,x in ls and enumerate(ls):
    print(x, f'  :random number between {(ind+1)*0+1}-{(ind+1)*1+1}')
