 
# Student Sports Management System
# Riviera High School Campus

def register_student():
    print("\n--- Student Registration ---")

    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    age = int(input("Enter student age: "))

    print("\nChoose your sport:")
    print("1. Football")
    print("2. Basketball")
    print("3. Volleyball")
    print("4. Athletics")
    print("5. Swimming")

    sport_choice = input("Enter your sport choice (1-5): ")

    match sport_choice:
        case "1":
            sport = "Football"
        case "2":
            sport = "Basketball"
        case "3":
            sport = "Volleyball"
        case "4":
            sport = "Athletics"
        case "5":
            sport = "Swimming"
        case _:
            sport = "Not selected"

    print("\n--- Registration Details ---")
    print("Name:", name)
    print("Student ID:", student_id)
    print("Age:", age)
    print("Sport:", sport)
    print("Registration completed!")


def check_eligibility():
    age = int(input("Enter student age: "))

    if age < 13:
        print("Junior sports category.")
    elif age <= 17:
        print("Student sports category.")
    else:
        print("Senior sports category.")


def calculate_performance():
    score = float(input("Enter performance score (0-100): "))

    if score < 0 or score > 100:
        print("Invalid score. Enter a score from 0 to 100.")
    elif score >= 80:
        print("Excellent performance!")
    elif score >= 60:
        print("Good performance!")
    elif score >= 40:
        print("Average performance.")
    else:
        print("Needs improvement.")


def main():
    while True:
        print("\n================================")
        print(" STUDENT SPORTS MANAGEMENT")
        print(" RIVIERA HIGH SCHOOL CAMPUS")
        print("================================")
        print("1. Register Student")
        print("2. Check Sports Eligibility")
        print("3. Calculate Performance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            register_student()
        elif choice == "2":
            check_eligibility()
        elif choice == "3":
            calculate_performance()
        elif choice == "4":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")


main()