def factorial(n):
    if n ==1:
        return 1
    return n*factorial(n-1)

def main():
    n = int(input("Enter a number: "))
    result= factorial(n)
    print(f"Factorial of  {n}  is {result}")
main()