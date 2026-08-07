def add_num(var1,var2):    

    var1=int(var1)
    var2=int(var2)
    sum=var1+var2
    return sum
      

def main():
    var1=input("Enter first number: ")
    var2=input("Enter second number: ")
    result=add_num(var1,var2)
    print(f"Sum of {var1} and {var2} is {result}")

main()