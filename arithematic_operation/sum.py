

def calculate(a,b):

    sum=a+b;
    mul=a*b;
    div=a/b;
    floor=a//b;
    mod=a%b;
    return f"sum={sum},mul={mul},div={div},floor={floor},mod={mod}"

def main():
    a=int(input("enter a:"));
    b=int(input("enter b:"));
    result=calculate(a,b)
    print(f"the result {result}")

main()