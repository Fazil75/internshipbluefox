def  greet(name, greeting="Hello"):
    return f"{greeting}, {name}"
def main():
    print(greet("sam"))
    print(greet("sam",greeting="hi"))
main()