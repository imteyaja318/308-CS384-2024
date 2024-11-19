from collections import defaultdict

# Initialize an empty dictionary to store student names and their grades
students = defaultdict(list)

def add_student(name, grades):
    name = name.lower()  # Convert name to lowercase for case insensitivity
    students[name] = grades

def update_grades(name, new_grades):
    """Update the grades of an existing student."""
    name = name.lower()  # Convert name to lowercase for case insensitivity
    if name in students:
        students[name] = new_grades
    else:
        print(f"Student '{name}' not found.")

def calculate_average(grades):
    return sum(grades) / len(grades) if len(grades) > 0 else 0

def print_averages():
    if not students:
        print("No students to display.")
        return

    #print("Students with their average grades:")
    for student, grades in students.items():
        average = calculate_average(grades)
        print(f"{student.capitalize()} - Average: {average:.2f}")

def sort_students_by_average():
    # Create a list of tuples (student, average)
    averages = [(student, calculate_average(grades)) for student, grades in students.items()]

    # Sort the list of tuples by average grade in descending order
    for i in range(len(averages)):
        for j in range(i + 1, len(averages)):
            if averages[j][1] > averages[i][1]:
                # Swap if the average grade of the second student is higher
                averages[i], averages[j] = averages[j], averages[i]

    # Print the sorted students with their average grades
    #print("\nSorted students by average grades:")
    for student, average in averages:
        print(f"{student.capitalize()} - Average: {average:.2f}")

def input_student_data():
    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        name = name.lower()  # Convert name to lowercase for consistency

        grades_input = input("Enter grades separated by commas: ").strip()
        try:
            grades = [int(grade.strip()) for grade in grades_input.split(',')]
            add_student(name, grades)
        except ValueError:
            print("Invalid input for grades. Please enter numbers separated by commas.")

def update_student_data():
    """Prompt the user to update the grades of an existing student."""
    name = input("Enter the name of the student to update: ").strip().lower()
    if name not in students:
        print(f"Student '{name}' not found.")
        return
    new_grades_input = input("Enter new grades separated by commas: ").strip()
    try:
        new_grades = [int(grade.strip()) for grade in new_grades_input.split(',')]
        update_grades(name, new_grades)
    except ValueError:
        print("Invalid input for grades. Please enter numbers separated by commas.")

def main():
    # Input student data
    input_student_data()

    # Print student averages
    print("\nStudents with their average grades:")
    print_averages()

    # Sort and print students by average grades
    print("\nSorted students by average grades:")
    sort_students_by_average()

    # Update student grades example
    print("\nUpdate student grades:")
    update_student_data()
    print("\nUpdated student grades:")
    print_averages()

if _name_ == "_main_":
    main()