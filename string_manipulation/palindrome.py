def palindrome(string):
    string=string.lower().replace(" ","")
    return string == string[::-1]
def main():
    string=input("enter the string:")
    result=palindrome(string)
    if result:
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")
main()