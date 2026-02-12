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


# -----------------------------
# Helper Function
# -----------------------------
def matric_exists(matric):
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                if line.strip().split(",")[0] == matric:
                    return True
    except FileNotFoundError:
        return False
    return False


# -----------------------------
# Add Student (with duplicate check)
# -----------------------------
def add_student():
    clear()
    header()
    print("ADD NEW STUDENT\n")

    name = input("Full Name      : ").strip()
    matric = input("Matric Number  : ").strip()
    dept = input("Department     : ").strip()
    level = input("Level          : ").strip()

    if not name or not matric:
        print("\n✗ Name and Matric Number are required.")
        pause()
        return

    if matric_exists(matric):
        print("\n✗ Error: Matric number already exists!")
        pause()
        return

    with open(FILE_NAME, "a") as f:
        f.write(f"{matric},{name},{dept},{level}\n")

    print("\n✓ Student record added successfully.")
    pause()


# -----------------------------
# View All Students
# -----------------------------
def view_students():
    clear()
    header()
    print("ALL STUDENTS\n")

    try:
        with open(FILE_NAME, "r") as f:
            print(f"{'Matric':<15}{'Name':<20}{'Dept':<15}{'Level':<10}")
            print("-" * 60)

            empty = True
            for line in f:
                matric, name, dept, level = line.strip().split(",")
                print(f"{matric:<15}{name:<20}{dept:<15}{level:<10}")
                empty = False

            if empty:
                print("No records found.")

    except FileNotFoundError:
        print("No records found.")

    pause()


# -----------------------------
# Search Student
# -----------------------------
def search_student():
    clear()
    header()
    print("SEARCH STUDENT\n")

    matric_no = input("Enter Matric Number: ").strip()
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
            print("\n✗ Student not found.")

    except FileNotFoundError:
        print("No records found.")

    pause()


# -----------------------------
# Delete Student
# -----------------------------
def delete_student():
    clear()
    header()
    print("DELETE STUDENT\n")

    matric_no = input("Enter Matric Number: ").strip()
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
            print("\n✗ Student not found.")

    except FileNotFoundError:
        print("No records found.")

    pause()


# -----------------------------
# Main Menu
# -----------------------------
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

        choice = input("Select Option: ").strip()

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
            print("\nInvalid option.")
            pause()


if __name__ == "__main__":
    main()

