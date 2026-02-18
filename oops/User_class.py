class User:
    def __init__(self,name,email,age,country="India"):
        self.name=name
        self.email=email
        self.age=age
        self.country=country
    def display(self):
        print(f"Name:{self.name}")
        print(f"Email:{self.email}")
        print(f"Age:{self.age}")
        print(f"Country:{self.country}")
        
u1=User("Salman","salman123@gmail.com",19,"Brazil")
u2=User("Arun","arun123@gmail.com",19)
u1.display()
print("------")
u2.display()
