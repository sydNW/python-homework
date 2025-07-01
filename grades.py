
import math

def get_student_info() -> tuple[list[str], list[float]]:
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    student_names = []
    student_scores = []

    print("\nEnter student names and scores:")

    for i in range(num_students):
        name = input(f"Student {i + 1}'s name: ").strip() or f"Student{i + 1}"
        student_names.append(name)

        while True:
            try:
                score = float(input(f"Enter {name}'s score: "))
                if 0 <= score <= 100:
                    student_scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid score. Please enter a valid number.")

    return student_names, student_scores


def determine_grade(score: float) -> str:
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


def calculate_average(scores: list[float]) -> float:
    return round(sum(scores) / len(scores), 2)


def display_results(names: list[str], scores: list[float]) -> None:
    print("\n=== Results ===")
    print(f"{'Name':<15} {'Score':<10} {'Grade'}")
    print("-" * 30)

    for name, score in zip(names, scores):
        grade = determine_grade(score)
        print(f"{name:<15} {score:<10.2f} {grade}")

    average = calculate_average(scores)
    print(f"\nClass Average: {average}")
    print(f"Rounded Up: {math.ceil(average)}")
    print(f"Rounded Down: {math.floor(average)}")


def run_grading_system():
    print("=== Grading System ===")
    course_name = "Data Structures and Algorithms"
    print(f"Course: {course_name}")

    while True:
        names, scores = get_student_info()
        display_results(names, scores)

        repeat = input("\nWould you like to grade another class? (yes/no): ").strip().lower()
        if repeat != "yes":
            print("Thanks for using the grading system!")
            break


if __name__ == "__main__":
    run_grading_system()
