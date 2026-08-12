def fruits_list():
    fruits=["apple", "banana", "orange", "grape", "kiwi"]
    fruits.append("mango")
    fruits.pop(1)
    return fruits

def main():
    result=fruits_list()
    print(result)
main()