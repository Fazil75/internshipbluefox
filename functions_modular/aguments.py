def avg(*arg):
    total = 0
    for i in arg:
        total += i
    return total/len(arg)

def main():
    arg = (4, 8, 15, 16)
    result =avg(*arg)
    print(f"result= {result}")
main()
    