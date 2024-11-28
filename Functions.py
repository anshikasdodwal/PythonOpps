#Functions: 
print("1. No Parameter and No Return Value")
class Calculator:
    def __init__(self):
        self.a=10
        self.b=20

    def display(self):
        x=100
        y=200
        z=x+y 
        print("Sum is: ",z)

c1=Calculator()
print(c1.a)
print(c1.b)
c1.display()

print("2.No Parameter and return value ")
class Calculator:
    def __init__(self):
        self.a=10
        self.b=20
    def display(self):
        x=100
        y=200
        z=x+y
        return z

c2=Calculator()
print(c2.a)
print(c2.b)
res=c2.display()
print("Sum is: ",res)

print("3. Parameter with No Return Type")
class Calculator:
    def __init__(self):
        self.a=10
        self.b=20
    def display(self,x,y):
        z=x+y
        print("Sum is: ",z)
c3=Calculator()
print(c3.a)
print(c3.b)
c3.display(100,200)


print("4. Parameter and Return Type")
class Calculator:
    def __init__(self):
        self.a=10
        self.b=20
    def display(self,x,y):
        z=x+y
        return z
c4=Calculator()
print(c4.a)
print(c4.b)
print("Sum is:" ,c4.display(100,200))
    

