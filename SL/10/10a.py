from functools import reduce
l1=[1,2,3,4,5]

l2=[x*3 for x in l1]
print("new list is",l2)

s1=reduce(lambda x,y:x+y,l1)
s2=reduce(lambda x,y:x+y,l2)

print("Sum of l1 is:",s1,"and of l2 is:",s2)

print("Total Sum is",s1+s2)
