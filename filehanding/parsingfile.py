def count_words():
    with open("note.txt","r") as files:
        data = files.read()
    words= data.split()
    return len(words)
def main():
    result= count_words()
    print(result)
main()

