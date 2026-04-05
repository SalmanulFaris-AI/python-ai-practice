import pandas as pd
import numpy as np

# Custom Series With index
a=pd.Series(["P","Q","R","S","T"],index=["1","2","3","4","5"])
print("Custom Series:")
print(a)

# Series from numpy array
arr = np.arange(100,150)
s=pd.Series(arr)
print("\nFull Series:")
print(s)

#Head and Tail

print("\nHead:")
print(s.head())

print("\nHead(3):")
print(s.head(3))

print("\nTail:")
print(s.tail())

print("\nTail(8):")
print(s.tail(8))

#Indexing

print("\nIndexing:")
print(s[38])
print(s[29])

#slicing

print("\nSlicing:")
print(s[44:48])
print(s[22:29])
