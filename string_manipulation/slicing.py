def remove(s,n):
    return s[n:]
def main():
    s=input("enter the string:")
    n=int(input("enter the number:"))
    result=remove(s,n)
    print(f"after removing {n} characters the string is {result}")
main()
