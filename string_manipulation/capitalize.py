def captial(string):
    words= string.split()
    for i in range(len(words)):
        words[i]= words[i][0].upper() + words[i][1:]
    return " ".join(words)
def main():
    string=input("enter the string:")
    result=captial(string)
    print(result)
main()