class Strings:
    def __init__(self,str):
        self.str=str
        self.count=0
    
    def reverse(self):
        arr=self.str.split(" ")
        s=''

        for i in reversed(arr):
            s+=i
            s+=" "
        
        print("\nreverse of 'I am Here' is:",s)

    def vowel(self):
        for i in self.str:
            if i=='a' or i=='e' or i=='i'or i=='o'or i=='u':
                self.count+=1
        

s=Strings('I am here')
s.reverse()


s1=input("enter string 1:")
s2=input("enter string 2:")
s3=input("enter string 3:")

obj1=Strings(s1)
r1=obj1.str[::-1]
obj1.vowel()


obj2=Strings(s2)
r2=obj2.str[::-1]
obj2.vowel()

obj3=Strings(s3)
r3=obj3.str[::-1]
obj3.vowel()

mydict={
    obj1.count:r1,
    obj2.count:r2,
    obj3.count:r3
}

print(sorted(mydict.items(),key=lambda x:x[0],reverse=True))


