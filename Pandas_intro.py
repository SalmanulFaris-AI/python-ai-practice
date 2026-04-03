import pandas as pd
# Series example
a=pd.Series([10,20,30,40])
print("\nSeries 1:")
print(a)

#DataFrame example
Data={"Name":["Ali","sara","john"],"Age":[25,22,30],"City":["Dubai","London","Usa"]}
df=pd.DataFrame(Data)
print("\nDataFrame:")
print(df)

#Another series 
b=pd.Series([5,10,15,20])
print("\nSeries 2:")
print(b)
