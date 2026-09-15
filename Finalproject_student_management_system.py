import csv
import os
from datetime import datetime

FILE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "students.csv"
)
# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Name", "Age", "Course", "Marks", "Date"])
# Add a new student
def add_student():
    print("\n========== ADD STUDENT ==========")
    student_id = input("Enter Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            for student in reader:
                if student["Student ID"] == student_id:
                    print("Student ID already exists.")
                    return
        name = input("Enter Student Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        age = int(input("Enter Age: "))
        if age <= 0:
            print("Age must be greater than 0.")
            return
        course = input("Enter Course: ").strip()
        if not course:
            print("Course cannot be empty.")
            return
        marks = float(input("Enter Marks: "))
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return
        date = datetime.now().strftime("%d-%m-%Y")
        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([student_id, name, age, course, marks, date])
        print("Student added successfully!")
    except ValueError:
        print("Invalid input! Please enter numbers for age and marks.")
    except Exception as e:
        print("An error occurred:", e)
# View all students
def view_students():
    print("\n========== ALL STUDENTS ==========")
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            students = list(reader)
            if not students:
                print("No student records found.")
                return
            print("-" * 90)
            print(f"{'ID':<10}{'Name':<20}{'Age':<8}{'Course':<20}{'Marks':<10}{'Date':<12}")
            print("-" * 90)
            for student in students:
                print(
                    f"{student['Student ID']:<10}"
                    f"{student['Name']:<20}"
                    f"{student['Age']:<8}"
                    f"{student['Course']:<20}"
                    f"{student['Marks']:<10}"
                    f"{student['Date']:<12}"
                )
            print("-" * 90)
    except FileNotFoundError:
        print("Student file not found.")
    except Exception as e:
        print("An error occurred:", e)
# Search for a student
def search_student():
    print("\n========== SEARCH STUDENT ==========")
    student_id = input("Enter Student ID to search: ").strip()
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            for student in reader:
                if student["Student ID"] == student_id:
                    print("\nStudent Found!")
                    print("Student ID :", student["Student ID"])
                    print("Name       :", student["Name"])
                    print("Age        :", student["Age"])
                    print("Course     :", student["Course"])
                    print("Marks      :", student["Marks"])
                    print("Date Added :", student["Date"])
                    return
            print("Student not found.")
    except FileNotFoundError:
        print("Student file not found.")
    except Exception as e:
        print("An error occurred:", e)
# Update student details
def update_student():
    print("\n========== UPDATE STUDENT ==========")
    student_id = input("Enter Student ID to update: ").strip()
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            students = list(reader)
        found = False
        for student in students:
            if student["Student ID"] == student_id:
                found = True
                print("\nEnter new details:")
                name = input("Enter Name: ").strip()
                age = int(input("Enter Age: "))
                course = input("Enter Course: ").strip()
                marks = float(input("Enter Marks: "))
                if age <= 0:
                    print("Age must be greater than 0.")
                    return
                if marks < 0 or marks > 100:
                    print("Marks must be between 0 and 100.")
                    return
                student["Name"] = name
                student["Age"] = age
                student["Course"] = course
                student["Marks"] = marks
                break
        if found:
            with open(FILE_NAME, "w", newline="") as file:
                fieldnames = ["Student ID", "Name", "Age", "Course", "Marks", "Date"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(students)
            print("Student details updated successfully!")
        else:
            print("Student not found.")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except FileNotFoundError:
        print("Student file not found.")
    except Exception as e:
        print("An error occurred:", e)
# Delete a student
def delete_student():
    print("\n========== DELETE STUDENT ==========")
    student_id = input("Enter Student ID to delete: ").strip()
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            students = list(reader)
        new_students = [
            student for student in students
            if student["Student ID"] != student_id
        ]
        if len(new_students) == len(students):
            print("Student not found.")
            return
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["Student ID", "Name", "Age", "Course", "Marks", "Date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_students)
        print("Student deleted successfully!")
    except FileNotFoundError:
        print("Student file not found.")
    except Exception as e:
        print("An error occurred:", e)
# Calculate average marks
def calculate_average():
    print("\n========== AVERAGE MARKS ==========")
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            students = list(reader)
            if not students:
                print("No student records available.")
                return
            total_marks = sum(float(student["Marks"]) for student in students)
            average = total_marks / len(students)
            print(f"Total Students : {len(students)}")
            print(f"Average Marks  : {average:.2f}")
    except FileNotFoundError:
        print("Student file not found.")
    except Exception as e:
        print("An error occurred:", e)
# Find the student with highest marks
def show_top_student():
    print("\n========== TOP STUDENT ==========")
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            students = list(reader)
            if not students:
                print("No student records available.")
                return
            top_student = max(students, key=lambda student: float(student["Marks"]))
            print("Top Student")
            print("Student ID :", top_student["Student ID"])
            print("Name       :", top_student["Name"])
            print("Course     :", top_student["Course"])
            print("Marks      :", top_student["Marks"])
    except FileNotFoundError:
        print("Student file not found.")
    except Exception as e:
        print("An error occurred:", e)
# Main menu
def main():
    create_file()
    while True:
        print("\n========================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Average Marks")
        print("7. Show Top Student")
        print("8. Exit")
        print("========================================")
        choice = input("Enter your choice (1-8): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            calculate_average()
        elif choice == "7":
            show_top_student()
        elif choice == "8":
            print("\nThank you for using Student Management System!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 8.")
# Program execution
if __name__ == "__main__":
    main()