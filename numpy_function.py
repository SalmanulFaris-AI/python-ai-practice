import numpy as np

# 1D Array
a = np.array([10,20,30,40])

print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Max:", np.max(a))
print("Min:", np.min(a))
print("Std:", np.std(a))

# Another array
b = np.array([5,10,15,20,25])

print("Sum:", np.sum(b))
print("Mean:", np.mean(b))
print("Max:", np.max(b))
print("Min:", np.min(b))

# 2D Array
a = np.array([[1,2,3],[4,5,6]])

print("Array:")
print(a)

print("Total Sum:", np.sum(a))
print("Column Sum:", np.sum(a,axis=0))
print("Row Sum:", np.sum(a,axis=1))
