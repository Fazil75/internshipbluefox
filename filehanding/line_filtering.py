def count_keywords(word):
    count = 0
    with open("note.txt","r") as file:
        for line in file:
            if word.lower() in line.lower():
                count += 1
    return count

def main():
    word = input("Enter a word: ")
    result = count_keywords(word)
    print(f"The word '{word}' appears {result} times in the file.")
main()