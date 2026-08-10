def counts(n):
    steps=0
    while n != 1:
        if n%2==0:
            n=n/2
        else:
            n=3*n+1 
        steps= steps + 1
    return steps
def main():
    n=int(input("enter the number:"))
    result=counts(n)
    print(f"the steps count is {result}")
main()