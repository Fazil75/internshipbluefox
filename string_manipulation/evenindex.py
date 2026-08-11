def even_index(string):
    for i in range(len(string)):
        if i % 2 == 0:
            print(string[i],end=" ")

def main():
    string=input("enter the string:")
    even_index(string)
main()