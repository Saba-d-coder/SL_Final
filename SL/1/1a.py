l=[]

print("Enter 5 items into list\n")

for i in range(5):
    l.append(int(input()))

print("\nYour list is:",l)

print("\nMax element is:",max(l),"\nMin element is:",min(l))

l.append(-4)
print("\nYour list after adding -4 is:",l)

l.remove(23)
print("\nYour list after removing 23 is:",l)

print("\nEnter element to check if its present in list:")

if int(input()) in l:
    print("\nIt's present")
else:
    print("\nIt's not present")



