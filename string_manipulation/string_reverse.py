def reverse(string):
    return string[::-1]
def main():
    string=input("enter the string:")
    result=reverse(string)
    print(f"The reverse of the string is {result}")
main()