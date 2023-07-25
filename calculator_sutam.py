print("----------  Calculator ---------------")
print("Choose 1 for Addition")
print("Choose 2 for Substraction")
print("Choose 3 for Multiplication")
print("Choose 4 for Division")
print("---------- Entering into the Program -----------")
class calculator:
    def calc(a,b,c):
        if(c==1):
            ans = int(a+b)
            print(ans)
            print("Checking that the ans is odd / Even : ")
            calculator.oddEven(ans)
        elif(c==2):
            ans = a-b
            print(ans)
            print("Checking that the ans is odd / Even : ")
            calculator.oddEven(ans)
        elif(c==3):
            ans = a*b
            print(ans)
            print("Checking that the ans is odd / Even : ")
            calculator.oddEven(ans)
        elif(c==4):
            ans = a/b
            print(ans)
            print("Checking that the ans is odd / Even : ")
            calculator.oddEven(ans)
        else:
            print("Please choose 1 to 4 ..")
    def oddEven(ans):
        if(int(ans)%2==0):
            print("The number is Even")
        else:
            print("The number is Odd")
class main:
    def main():
        a = int(input("Enter 1st number : "))
        b = int(input("Enter 2nd number : "))
        c = int(input("Enter your choice : "))
        calculator.calc(a,b,c)
        print("--------End of the Program---------")
        
main.main()