def main():
    with open("file.txt","w") as file:
        file.write("first line\n")
        file.write("second line\n")
        file.write("third line\n")

    with open("file.txt","r") as file:
        content=file.read()
    print(content)
main()