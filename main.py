import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT,
    email TEXT
)
""")
conn.commit()

# Add Student
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    email = input("Enter Email: ")

    cur.execute("INSERT INTO students (name, age, course, email) VALUES (?, ?, ?, ?)",
                (name, age, course, email))
    conn.commit()
    print("✅ Student Added Successfully!\n")

# View Students
def view_students():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    print("\n--- Student List ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}, Email: {row[4]}")
    print()

# Update Student
def update_student():
    id = int(input("Enter Student ID to Update: "))
    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    course = input("Enter New Course: ")
    email = input("Enter New Email: ")

    cur.execute("""
    UPDATE students
    SET name=?, age=?, course=?, email=?
    WHERE id=?
    """, (name, age, course, email, id))
    conn.commit()
    print("✅ Student Updated Successfully!\n")

# Delete Student
def delete_student():
    id = int(input("Enter Student ID to Delete: "))
    cur.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    print("🗑️ Student Deleted Successfully!\n")

# Search Student
def search_student():
    keyword = input("Enter Name to Search: ")
    cur.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + keyword + '%',))
    rows = cur.fetchall()

    print("\n--- Search Results ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}, Email: {row[4]}")
    print()

# Menu
def menu():
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            search_student()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice!\n")

# Run program
menu()

# Close connection
conn.close()
