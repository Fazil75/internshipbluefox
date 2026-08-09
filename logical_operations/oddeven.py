def odd_even(n):
    return "even" if n%2 == 0 else "odd"

def main():
    n=int(input("enter the number:"))
    result=odd_even(n)
    print(f"the number {n} is {result}")

main()