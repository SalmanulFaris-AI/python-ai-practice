#Method Overriding
class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def start(self):
        print("Car starts with key")
class Bike(Vehicle):
    def start(self):
        print("Bike starts with kick")
v=Vehicle()
c=Car()
b=Bike()
v.start()
c.start()
b.start()
print("loop test")
for vehicle in [v,c,b]:
    vehicle.start()
    
