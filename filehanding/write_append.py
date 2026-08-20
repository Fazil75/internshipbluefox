def mode():
    with open("text,txt","w") as file:
        file.write("first line\n")

    with open("text,txt","w") as file:
            file.write("second line\n")

    with open("text,txt","a") as file:
            file.write("third line\n")
    with open("text,txt","a") as file:
            file.write("fourth line\n")

def main():
    mode()

    with open("text,txt","r") as file:
        print(file.read())
main()