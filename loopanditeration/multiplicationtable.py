def mult_table(n):
    for i in range(1,11):    
        print(f"Row {i}: ", end="")

        for j in range(1, 11):
            print(i * j, end=" ")
        
def main():
    n=int(input("enter the number:"))
    mult_table(n)

main()