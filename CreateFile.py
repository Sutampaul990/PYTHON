b=input("Enter yout file name : ")
y=input("Enter the File Contents : ")
f=open(b,"w") # r -> read operation
f.write(y)
f.close()
print("File created successfully")