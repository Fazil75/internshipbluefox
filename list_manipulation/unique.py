def unique_list(n):
    unique=[]
    for i in n:
        if i not in unique:
            unique.append(i)
    return unique

def main():
    n=list(map(int,input("enter the numbers: ").split()))
    result=unique_list(n)
    print(f"list: {n}")
    print(f"Unique list: {result}") 
main()