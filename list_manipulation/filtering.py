def filtering(n):
    filter=[]
    for i in n:
        if i%5==0:
            filter.append(i)
    return filter

def main():
    n=list(map(int,input("enter the numbers: ").split()))
    print(f"list: {n}")
    result=filtering(n)
    print(f"filtered list : {result}")
main()


