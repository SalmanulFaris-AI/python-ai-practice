from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.141*self.radius**2
        
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
        
c=Circle(5)
r=Rectangle(10,5)
print("Circle Area:",c.area())
print("Circle Area:",r.area())

