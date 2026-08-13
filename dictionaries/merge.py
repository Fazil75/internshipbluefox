def merge_dict(dict1,dict2):
    combined = dict1.copy()
    combined.update(dict2)
    return combined

def main():
    dict1 ={"name":"john","age":25}
    dict2 ={"age":26,"city":"new york"}
    result = merge_dict(dict1,dict2)
    print(f"merged dictionary: {result}")
main()
