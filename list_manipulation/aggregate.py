def values(n):
    largest=n[0]
    smallest=n[0]
    for i in n:
        if i>largest:
            largest=i   

        if i<smallest:
            smallest=i  
    return largest,smallest

def main():
    n=list(map(int,input("enter the numbers: ").split()))
    largest,smallest=values(n)
    print(f"Largest: {largest}, Smallest: {smallest}")
main()
