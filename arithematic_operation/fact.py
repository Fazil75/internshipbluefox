def factorial(var1):

    fact = 1
    for i in range(1, var1 + 1):
        fact = fact * i
    return fact
def main(): 
    var1=int(input("Enter a number: "))
    result= factorial(var1)
    print(f"Factorial of {var1} is {result}")
main()