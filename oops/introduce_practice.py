class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print("My Name is",self.name,"and Iam",self.age,"years old.")
        
s1=Student("Salman",18)
s1.introduce()
