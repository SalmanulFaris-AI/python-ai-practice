#Practice 1:student class example
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("NAME:",self.name)
        print("MARKS:",self.marks)
s1=student("salman",95)
s1.display()
s1=student("anoop",89)
s1.display()
# practice 2: car class example
class cars:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def show_details(self):
        print("BRAND NAME:",self.brand)
        print("SPEED OF CAR:",self.speed)
car1=cars("BENZ",210)
car2=cars("VOLVO",230)
car1.show_details()
car2.show_details()
