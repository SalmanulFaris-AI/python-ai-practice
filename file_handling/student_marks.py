name = input("Enter student name:")
marks =input("enter marks:")

with open("marks.txt","a")as f:
    f.write(name+","+marks+"\n")
print("Record saved")
