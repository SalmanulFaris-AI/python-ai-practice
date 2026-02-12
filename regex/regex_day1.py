# check if word "data"exist in text
import re
text = "my name is salmanul faris and iam learning data science"
result =re.search("data",text)
print(result)

# extract all numbers
data = "My score are 78 and 92"
print(re.findall(r"\d",data))

# chech if string starts with "AI"
nums= "AI & python is very important"
if re.search("^AI",nums):
    print("Yes")
else:
    print("no")
    
#Find all words ending with "ing"
t= "I am learning coding and building projects"
print(re.findall(r"\w+ing",t))
