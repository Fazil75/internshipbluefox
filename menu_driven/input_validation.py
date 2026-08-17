def calculator(choice,num1,num2):
      
      if choice == 1:
         print("result=",num1+num2)
      elif choice == 2:
         print("result=",num1-num2)
      elif choice == 3:
         print("result=",num1*num2)
      elif choice == 4:
         if num2 == 0:
            print("Error: Division by zero")
         else:
            print("result=",num1/num2)
      else:
         print("Invalid choice")
      return choice,num1,num2
def main():
   while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice =int(input("Enter your choice: "))
    if choice < 1 or choice > 5:
        print("Invalid choice,try again")
        continue
    if choice == 5:
        print("exiting")
        break
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    calculator(choice,num1,num2)
main()


