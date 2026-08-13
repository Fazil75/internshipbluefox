def report_card(student,name):
    print(f"Report card for {name}:")
    for subject in student[name]:
        grade = student[name][subject]
        print(f"subject: {subject}, grade: {grade}")
def main():
    student = {"Alice": {"Math": 85, "Science": 90},}
    report_card(student, "Alice")
main()