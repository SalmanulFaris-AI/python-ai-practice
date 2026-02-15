class Bank:
    def __init__(self,balance):
        self.__balance=balance  #private variable
    def deposit(self,amount):
        self.__balance+=amount
        print("deposite:",amount)
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print("withdrawn:",amount)
        else:
            print("insufficient balance")
    def get_balance(self):
        return self.__balance
b1=Bank(1000)
b1.deposit(500)
b1.withdraw(300)
print("current balance:",b1.get_balance())


# creat User acoount Class
class UserAccount:
    def __init__(self,username,password):
        self.username=username
        self.__password=password      #private
    def check_password(self,pass_input):
        if pass_input==self.__password:
            print("Access granated")
        else:
            print("wrong password")
    def change_password(self,old_pass,new_pass):
        if old_pass==self.__password:
            self.__password=new_pass
            print("password changed successfully")
        else:
            print("Old password incorrect")
    def display_user(self):
        print("Username:",self.username)
        
#Creat useraccount Object

u1=UserAccount("salman","1234")
u1.display_user()
u1.check_password("1234")
u1.change_password("1234","abcd")
u1.check_password("abcd")
print(u1.username)
