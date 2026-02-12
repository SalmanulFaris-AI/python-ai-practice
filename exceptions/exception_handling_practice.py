try:
    n=int(input("enter a number"))
    print("100 divided by n =",100/n)
except ZeroDivisionError:
    print("cannot divided by zero")
except ValueError:
    print("invalid input-enter number only")
finally:
    print("program finished")
