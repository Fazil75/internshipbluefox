def rotate(numbers,n):
    return numbers[n:] + numbers[:n]


def main(): 
    
    numbers = list(map(int,input("enter the list: ").split()))
    n = int(input("enter the number of rotation: "))
    print(f"list: {numbers}")
    result = rotate(numbers,n)
    print(f"rotated list: {result}")
main()