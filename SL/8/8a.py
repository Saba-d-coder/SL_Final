dic={
    "Hydrogen":"H",
    "Helium":"He",
    "Lithium":"li"
}

ele,sym=input("Enter an element and its symbol separated by space").split(" ")

dic[ele]=sym
print("\nYour dictionary is",dic)

ele,sym=input("Enter a duplicate element and its symbol separated by space").split(" ")

dic[ele]=sym
print("\nYour dictionary looks like",dic)

print("\nTotal number of atomic elements are:",len(dic))

ch=input("Enter element to be be searched")

if ch in dic.keys():
    print("\nElement present in dictionary. It's symbol is->",dic[ch])
else:
    print("\nNot Found")

