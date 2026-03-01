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


## Two Dimensional Arrays

import numpy as np

#Creating 2D array from list
a= np.array([[10,20],[30,40]])
print("2D Array:\n",a)

#Creating using arange and reshape
b=np.arange(1,13).reshape(3,4)
print("Reshape array:\n",b)

#Creating zeros 2D arrays
z=np.zeros((2,5))
print("Zeros Array:\n",z)

#Accessing elements
print("Element at row 2,column 3 =",b[2,3])
print("Second column:\n",b[:,2])
