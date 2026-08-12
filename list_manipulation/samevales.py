def boundary(n):
    return n[0] == n[-1]
def main():
    n=list(map(int,input("enter the numbers: ").split()))
    result=boundary(n)
    print(result)
main()