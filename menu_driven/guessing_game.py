import random

def guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    print("i have guessed a number between 1 and 100")

    while True:
        guess= int(input("guess the number: "))
        attempts += 1

        if guess < number:
            print("too low")
        elif guess > number:
            print("too high")
        else:
            print(f"you guessed it right in {attempts} attempts")   
            return attempts
def main():
    high_score = None
    while True:
        print("1. play")
        print("2. view high score")
        print("3. exit")
        choice = input("enter your choice: ")

        if choice == "1":
            score = guessing_game()
            if high_score is None or score < high_score:
                high_score = score
                print("new high score")
            else:
                print("you did not beat the high score")
        elif choice == "2":
            if high_score is None:
                print("no high score yet")
            else:
                print(f"the high score is {high_score}")
        elif choice == "3":
            print("exiting..")
            break
        else:
            print("invalid choice")
main()
        



