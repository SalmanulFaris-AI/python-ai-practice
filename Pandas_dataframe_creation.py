 # PREPARING DATAFRAME
import pandas as pd
# Using Nested list
lst=[["Radha",23,"Engineer"],["Manu",43,"Advocate"],["Sonu",32,"Doctor"],["Vinu",26,"Architect"]]
df=pd.DataFrame(lst,columns=["Name","Age","Profession"])
print(df)

#Using List of dictionaries

lst=[{"Name":"Radha","Age":23,"Profession":"Engineer"},{"Name":"Manu","Age":43,"Profession":"Advocate"},
     {"Name":"Sonu","Age":32,"Profession":"Doctor",},{"Name":"Vinu","Age":26,"Profession":"Architect"}]
df1=pd.DataFrame(lst)
print(df1)

#Using dictionarary of list

lst={"Name":["Radha","Manu","Sonu","Vinu"],"Age":[23,43,32,26],"Profession":["Engineer","Advocate","Doctor","Architect"]}
df2=pd.DataFrame(lst)
print(df2)
