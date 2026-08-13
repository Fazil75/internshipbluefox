def common(list1,list2):
    set1 = set(list1)
    set2 = set(list2)   
    return set1 & set2
def main():
    list1 = list(map(int,input("enter the first list: ").split()))
    list2 = list(map(int,input("enter the second list: ").split())) 
    print(f"list1: {list1}")
    print(f"list2: {list2}")    
    result = common(list1,list2)
    print(f"common elements: {result}")
main()