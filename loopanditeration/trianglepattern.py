def triangle(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i , end=" ")
        print()
def main():
    n=int(input("enter the number:"))
    triangle(n) 
main()