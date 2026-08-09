import time
def timer(n):
    while n>0:
        print(n,end=" ")
        time.sleep(1)
        n = n-1
        if n==0:
            print("blast")


def main():
    n=int(input("enter the number:"))
    timer(n)
main()

