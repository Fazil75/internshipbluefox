def dict_count(dict1):
    words = dict1.split()
    counts ={}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
    
def main():
    dict1 =input("enter the dictionary: ")
    result = dict_count(dict1)  
    print(result)
    
main()
    
