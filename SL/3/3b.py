from collections import Counter
import sys
from functools import reduce

dic,sortedDic,list={},{},[]

with open(sys.argv[1]) as f:
    for word in f.read().split():
        if word not in dic:
            dic[word]=1
        else:
            dic[word]+=1

print("\nYour freq dic is:",dic)

sortedDic=sorted(dic.items(),key=lambda s:s[1],reverse=True)
print("\nSorted dictionary is:",sortedDic,"\n")

for i in dic.keys():
    list.append(len(i))

print("Length of all words are:",list,"\n")

sum=reduce((lambda x,y:x+y),list)
print("Average is:",sum/len(list),"\n")

print("Sqaures are:",[x*x for x in list if x%2!=0])




