# Define a list to store student records
students = []

# Function to add student information
def add_student():
    rollno = input("Enter Your Roll Number: ")
    name = input("Enter The Student Name: ")
    marks = float(input("Enter The Marks: "))
    student = {'rollno': rollno, 'name': name, 'marks': marks}
    students.append(student)
    print(f"Student {name} added successfully.")

# Function to display all student information
def display_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\nStudent Records:")
        for student in students:
            print(f"Roll Number: {student['rollno']}, Name: {student['name']}, Marks: {student['marks']}")
        print()

# Function to search for a student by roll number
def search_student():
    rollno = input("Enter Roll Number to search: ")
    found = False
    for student in students:
        if student['rollno'] == rollno:
            print(f"\nStudent Found: Roll Number: {student['rollno']}, Name: {student['name']}, Marks: {student['marks']}")
            found = True
            break
    if not found:
        print(f"No student found with Roll Number {rollno}.\n")

# Function to remove a student by roll number
def remove_student():
    rollno = input("Enter Roll Number to remove: ")
    for student in students:
        if student['rollno'] == rollno:
            students.remove(student)
            print(f"Student with Roll Number {rollno} has been removed.")
            return
    print(f"No student found with Roll Number {rollno}.\n")

# Function to display total number of student records
def total_students():
    print(f"Total number of students: {len(students)}\n")

# Main function to display menu and interact with the user
def menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student Information")
        print("2. Display All Student Information")
        print("3. Search Student by Roll Number")
        print("4. Remove Student by Roll Number")
        print("5. Display Total Number of Students")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            remove_student()
        elif choice == '5':
            total_students()
        elif choice == '6':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Start the program by calling the menu function
if __name__ == "__main__":
    menu()
