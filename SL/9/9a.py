class student:
    def __init__(self,n,a,li):
        self.name=n
        self.age=a
        self.li=li

    def display(self):
        print("Name:",self.name,"\nAge:",self.age,"\nMarks:",self.li)


print("Student 1")
std1=student('KSK',20,[96,98,90])
std1.display()

print("\nStudent 2")
std2=student('Saba',21,[97,90,99])
std2.display()

print("\nEnter details of student:\n") 
n=input("Name:")
a=input("Age:")
l1=[]

print("\nEnter marks of 3 subjects:\n")
for i in range(3):
    l1.append(int(input()))

print("\nEntered student details")
s1=student(n,a,l1)
s1.display()



