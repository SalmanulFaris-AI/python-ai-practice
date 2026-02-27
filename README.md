import numpy as np

#creating array from list
a=np.array([10,20,30,40])
print("Array from list:",a)

#Using arrange()
b=np.arange(1,21)
print("1 to 20:",b)

#Using step
c=np.arange(5,55,5)
print("Step 5",c)

#Using linspace
d=np.linspace(0,20,5)
print("linspace:",d)

#Multiple array
print("Multiple by 3:",b*3)

#Using zeros
e=np.zeros(8)
print("Zeros:",e)
