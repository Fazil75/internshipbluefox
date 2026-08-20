import csv

def read_csv():
    with open("people.csv","r") as file:
        read= csv.reader(file)
        for row in read:
            name= row[0]
            age= row[1]
            print(f"name: {name} , age: {age}")
    

def main():
    read_csv()
main()