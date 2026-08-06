def greaterthan_equalto(var1, var2):
    if var1 >= var2:
        return f"{var1} is greater than {var2}"
    else:
        return f"{var2} is greater than {var1}"


def main():
    var1 = int(input("Enter first number: "))
    var2 = int(input("Enter second number: "))

    greater = greaterthan_equalto(var1, var2)

    print(greater)

main()