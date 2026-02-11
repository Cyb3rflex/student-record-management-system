import os

FILE_NAME = "students.txt"


def clear():
    os.system("clear" if os.name == "posix" else "cls")


def pause():
    input("\nPress Enter to continue...")


def header():
    print("=" * 60)
    print("      STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 60)


def add_student():
    clear()
    header()
    print("ADD NEW STUDENT\n")

    name = input("Full Name      : ")
    matric = input("Matric Number  : ")
    dept = input("Department     : ")
    level = input("Level          : ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{matric},{name},{dept},{level}\n")

    print("\n✓ Student record added successfully.")
    pause()


def view_students():
    clear()
    header()
    print("ALL STUDENTS\n")

    try:
        with open(FILE_NAME, "r") as f:
            print(f"{'Matric':<15}{'Name':<20}{'Dept':<15}{'Level':<10}")
            print("-" * 60)
            for line in f:
                matric, name, dept, level = line.strip().split(",")
                print(f"{matric:<15}{name:<20}{dept:<15}{level:<10}")
    except FileNotFoundError:
        print("No records found.")

    pause()


def search_student():
    clear()
    header()
    print("SEARCH STUDENT\n")

    matric_no = input("Enter Matric Number: ")
    found = False

    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                matric, name, dept, level = line.strip().split(",")
                if matric == matric_no:
                    print("\nStudent Found:")
                    print("-" * 30)
                    print(f"Name       : {name}")
                    print(f"Department : {dept}")
                    print(f"Level      : {level}")
                    found = True
                    break

        if not found:
            print("\nStudent not found.")
    except FileNotFoundError:
        print("No records found.")

    pause()


def delete_student():
    clear()
    header()
    print("DELETE STUDENT\n")

    matric_no = input("Enter Matric Number: ")
    deleted = False

    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()

        with open(FILE_NAME, "w") as f:
            for line in lines:
                if not line.startswith(matric_no + ","):
                    f.write(line)
                else:
                    deleted = True

        if deleted:
            print("\n✓ Record deleted successfully.")
        else:
            print("\nStudent not found.")

    except FileNotFoundError:
        print("No records found.")

    pause()


def main():
    while True:
        clear()
        header()
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        print("-" * 60)

        choice = input("Select Option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("\nExiting system...")
            break
        else:
            print("Invalid option.")
            pause()


if __name__ == "__main__":
    main()
