def inventory_system(choice,inventory):
    if choice == 1:
        items=input("Enter the items: ")
        quantity=int(input("Enter the quantity: "))

        if items in inventory:
            inventory[items] += quantity
        else:
            inventory[items] = quantity
            print("stock added")
    elif choice == 2:
        items=input("Enter the items: ")
        quantity=int(input("Enter the quantity: "))

        if items not in inventory:
            print("no stock")
        elif quantity> inventory[items]:
            print("not available")
        else :
            inventory[items] -= quantity 
            print("stock removed")
    elif choice == 3:
        if len(inventory) == 0:
            print("no stock")
        else:
            print(inventory)
    else:
        print("invalid choice")

def main():
    inventory={}
    while True:
        print("1. Add stock")
        print("2. Remove stock")
        print("3. View Inventory")
        print("4. Exit")
        choice=int(input("Enter your choice: "))
        if choice == 4:
            break
        else:
            inventory_system(choice,inventory)
main()

