import json

students = []

# دالة لتحميل البيانات من الملف
def load_data():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
            print("--> Data loaded successfully from file!\n")
    except FileNotFoundError:
        students = []

# دالة لحفظ البيانات فـ ملف
def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file)
    print("--> Data saved successfully to students.json!\n")

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter grade (out of 20): "))
    students.append({"name": name, "grade": grade})
    save_data() # حفظ تلقائي عند إضافة طالب

def display_students():
    if not students:
        print("--> The list is empty.\n")
        return
    print("\n--- Students List ---")
    for s in students:
        print(f"Name: {s['name']} | Grade: {s['grade']}/20")
    print("----------------------\n")

def calculate_average():
    if not students:
        print("--> No students to calculate average.\n")
        return
    total = sum(s['grade'] for s in students)
    avg = total / len(students)
    print(f"\n--> Class Average: {avg:.2f}/20\n")

def main():
    load_data() # تحميل البيانات عند بداية التشغيل
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Calculate Class Average")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            calculate_average()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("--> Invalid option, try again.\n")

main()