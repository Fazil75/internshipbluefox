def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False

def main():
    year =int(input("enter the year:"))
    result=leap_year(year)
    if result:
        print(f"{year} is a leap year") 
    else:
        print(f"{year} is not a leap year")         

main()
       