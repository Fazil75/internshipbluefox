def replace_space(string):
    return string.replace(" ", "_")
def main():
    string=input("enter the string:")
    result=replace_space(string)
    print(result)   
main()
