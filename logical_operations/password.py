def check_password(password):
    failed = []
    if len(password) < 8:
        failed.append("length")
    if not any(char.isdigit() for char in password):
        failed.append("digit")
    if not any(char.isupper() for char in password):
        failed.append("uppercase")
    
    return failed

def main():
    password = input("Enter a password: ")
    result = check_password(password)
    if result:
        print(f"Password is invalid. Failed : {', '.join(result)}")
    else:   
        print("Password is valid.")
main()