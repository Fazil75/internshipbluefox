def invert(dict1):
    inverted={}
    for key in dict1:
        inverted[dict1[key]]=key
    return inverted
def main():
    dict1 = {"a":1,"b":2,"c":3}
    result = invert(dict1)
    print(f"inverted dictionary: {result}")
main()


