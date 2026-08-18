def sum_avg(n):
    sum = 0
    for num in n:
        sum += num
    avg = sum/len(n) 

    return sum,avg

def main():
    n=list(map(int,input("Enter the number of elements: ").split()))
    print(n)
    result = sum_avg(n)
    print(f"result: {result}")
main()
    
