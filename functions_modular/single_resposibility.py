def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    options = """1.celsius to fahrenheit
    2.fahrenheit to celsius"""

    choice= int(input("enter the choice:"))

    temperature = float(input("enter the temperature:"))
    if choice == 1:
        print(celsius_to_fahrenheit(temperature))
    elif choice == 2:
        print(fahrenheit_to_celsius(temperature))   

main()