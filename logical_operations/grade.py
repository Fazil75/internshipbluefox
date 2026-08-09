def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    score =int(input("Enter the score: "))
    result= grade(score)
    print(f"The grade for score {score} is {result}")
main()