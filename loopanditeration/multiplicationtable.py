def mult_table(n):
    print(f"multiplication table of {n} is ")
    for i in range(1,11):
            print(n*i,end=" ")
    
        
def main():
    n=int(input("enter the number:"))
    mult_table(n)

main()