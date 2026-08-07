def incometax(income):
    if income <= 10000:
        return 0
    elif income <=20000:
        return (income - 10000) * .10
    else:
        return 10000 * .10 + (income - 20000)* .20 

def main():
    income=int(input("enter your income:"))
    result= incometax(income)
    print(f"the income tax is {result}")    

main()