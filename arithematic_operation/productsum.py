
def product_sum(a,b):
    if a*b>=1000:
        return a+b
    else:
        return a*b

def main():
    a=int(input("enter a:"));
    b=int(input("enter b:"));
    result=product_sum(a,b)
    print(f"the result ={result}")
main()