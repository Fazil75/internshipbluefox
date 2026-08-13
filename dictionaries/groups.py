def groups(words):
    groups={}
    for key in words:
        first = key[0]
        if first not in groups:
            groups[first] = []
        groups[first].append(key)
    return groups
def main():
    words = ["apple","banana","cherry","avocado","blueberry"]
    result = groups(words)
    print(f"grouped dictionary: {result}")
main()