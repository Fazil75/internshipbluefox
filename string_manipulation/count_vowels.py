def count_vowels(string):
    vowels= "aeiou"
    count=0
    for i in string: 
        if i.lower() in vowels:
            count += 1  
    return count
def main():
    string=input("enter the string:")
    result=count_vowels(string)
    print(f"The number of vowels in the string is {result}")
main()