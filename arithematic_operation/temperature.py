def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


choice = input("Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ")

temperature = float(input("Enter temperature: "))

if choice == "C":
    print("Fahrenheit =", celsius_to_fahrenheit(temperature))

elif choice == "F":
    print("Celsius =", fahrenheit_to_celsius(temperature))

else:
    print("Invalid choice")