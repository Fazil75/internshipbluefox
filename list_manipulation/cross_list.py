def cross_list(list1,list2):
    list3 = []
    for i in list1:
        if i % 2 != 0:
            list3.append(i)
    for i in list2:
        if i % 2 == 0:
            list3.append(i)
    return list3

def main():
    list1=list(map(int,input("enter the first list: ").split()))
    list2=list(map(int,input("enter the second list: ").split()))
    print(f"list1: {list1}")
    print(f"list2: {list2}")
    result=cross_list(list1,list2)
    print(f"crossed list : {result}")
main()