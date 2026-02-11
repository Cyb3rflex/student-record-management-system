import tkinter as tk
from tkinter import messagebox

FILE_NAME = "students.txt"


def add_student():
    name = entry_name.get()
    matric = entry_matric.get()
    dept = entry_dept.get()
    level = entry_level.get()

    if not name or not matric:
        messagebox.showwarning("Warning", "Name and Matric are required!")
        return

    with open(FILE_NAME, "a") as f:
        f.write(f"{matric},{name},{dept},{level}\n")

    messagebox.showinfo("Success", "Student Added Successfully")

    entry_name.delete(0, tk.END)
    entry_matric.delete(0, tk.END)
    entry_dept.delete(0, tk.END)
    entry_level.delete(0, tk.END)


def view_students():
    try:
        with open(FILE_NAME, "r") as f:
            records = f.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, records)
    except FileNotFoundError:
        messagebox.showinfo("Info", "No records found")


# GUI Setup
root = tk.Tk()
root.title("Student Record Management System")
root.geometry("500x500")
root.configure(bg="#f4f4f4")

tk.Label(root, text="Student Record Management System",
         font=("Arial", 14, "bold"),
         bg="#f4f4f4").pack(pady=10)

frame = tk.Frame(root, bg="#f4f4f4")
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Matric").grid(row=1, column=0)
entry_matric = tk.Entry(frame)
entry_matric.grid(row=1, column=1)

tk.Label(frame, text="Department").grid(row=2, column=0)
entry_dept = tk.Entry(frame)
entry_dept.grid(row=2, column=1)

tk.Label(frame, text="Level").grid(row=3, column=0)
entry_level = tk.Entry(frame)
entry_level.grid(row=3, column=1)

tk.Button(root, text="Add Student",
          command=add_student,
          bg="#4CAF50", fg="white").pack(pady=5)

tk.Button(root, text="View Students",
          command=view_students,
          bg="#2196F3", fg="white").pack(pady=5)

text_area = tk.Text(root, height=10, width=50)
text_area.pack(pady=10)

root.mainloop()
