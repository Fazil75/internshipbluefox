def bucket(n):
    odd=[]
    even=[] 
    for i in n:
        if i%2 == 0:
            even.append(i)  
        else:
            odd.append(i)
    return odd,even

def main():
    n=list(map(int,input("enter the numbers: ").split()))
    print(f"list: {n}")
    odd,even=bucket(n)
    print("Odd list:",odd)
    print("Even list:",even)
main()