class Student:
    def __init__(self):
        self.name="Anshika"
        self.age=20
        self.gender='F'
        self.add="Pune"
    
    def eat(self):
        print("Student is eating")
    def study(self):
        print("Student is studying")
s1=Student()
print(s1.name)
print(s1.age)
print(s1.gender)
print(s1.add)
s1.eat()
s1.study()
s2=Student()
print(s2.name)