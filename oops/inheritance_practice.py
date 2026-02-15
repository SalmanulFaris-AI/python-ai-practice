class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name:",self.name)
class Student(Person):
    def __init__(self,name,mark):
        super().__init__(name)
        self.mark=mark
    def show_marks(self):
        print("Marks:",self.mark)
s1=Student("salman",94)
s1.display()
s1.show_marks()

#making class of animal,dog and cat using inheritance
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Animal makes sound")
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        super().speak()
        print("Dog barks")
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        super().speak()
        print("cat meows")
        
d1=Dog("lassi")
d1.speak()
c1=Cat("calppo")
c1.speak()

# making class of employee and manager using inheritance
class Employee:
     def __init__(self,name,salary):
         self.name=name
         self.salary=salary
     def show_detailes(self):
         print("NAME:",self.name)
         print("SALARY:",self.salary)
class Manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus=bonus
    def show_total_salary(self):
        super().show_detailes()
        print("BONUS:",self.bonus)
        print("TOTAL SALARY=",self.salary+self.bonus)
        
e1=Employee("salman",40000)
e1.show_detailes()
m1=Manager("salman",40000,5000)
m1.show_total_salary()
