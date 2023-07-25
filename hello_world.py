# print ("Hello World")

class Loops:
    def ForLoops():
        x = int(input("Enter any Number : "))
        y = int(input("Enter any Number : "))
        for j in range (x,y+1,1):
            print(j,end=" ")
Loops.ForLoops()

arr_1 = [1,2,3,4,5]  # List
arr_2 = {1,2,3,4,5} # 
arr_3 = (1,2,3,4,5)  # Tuple
arr_4 = {
    "name" : "Test",
    "age" : 12,
    "type" : "All"
}
print(arr_1,type(arr_1))
print(type(arr_2))
print(type(arr_3))
print(type(arr_4))