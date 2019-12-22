class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    def area(self):
        a=self.l * self.b
        print('Area of rectangle is:',a)

r1=rectangle(2,5.6)
r1.area()

r1=rectangle(-2,10.6)
r1.area()

