def contacts_book(choice,contacts):
    if choice == 1:
        name=(input("Enter the name: "))
        phone=int(input("Enter the phone number: "))
        contacts[name]= phone
        print("contact added")
    elif choice == 2:
        name=(input("Enter the name: "))
        if name in contacts:
            print("Phone number of ",name," is ",contacts[name])
        else:
            print("Contact not found")
    elif choice == 3:
        name=(input("Enter the name: "))
        if name in contacts:
            del contacts[name]
            print("Contact deleted")
    elif choice == 4:
        print("Contacts: ")
        print(contacts)
    else:
        print("Invalid choice")
def main():
    contacts={}
    while True:
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. list contacts")
        print("5. Exit")
        choice=int(input("Enter your choice: "))
        if choice == 5:
            print("exiting..")
            break
        contacts_book(choice,contacts)
main()