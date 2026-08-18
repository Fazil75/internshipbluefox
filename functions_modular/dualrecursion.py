def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0

    return fibonacci(n-1) +fibonacci(n-2)

def main():
    n=int(input("Enter the number: "))
    result=fibonacci(n)
    print(result)
main()