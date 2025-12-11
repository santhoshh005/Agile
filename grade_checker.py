#!/usr/bin/env python3

def get_grade(score):
    if score >= 95:
        return 'A+'
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def get_grade_description(grade):
    descriptions = {
        'A+': 'Excellent - Outstanding performance',
        'A': 'Excellent - Very Good performance',
        'B': 'Good - Above average performance',
        'C': 'Average - Satisfactory performance',
        'D': 'Below Average - Passing performance',
        'F': 'Fail - Needs improvement'
    }
    return descriptions.get(grade, 'Unknown grade')

def display_menu():
    print("\n" + "="*50)
    print("       STUDENT GRADE CHECKER PROGRAM")
    print("="*50)
    print("1. Check grade for a single student")
    print("2. Check grades for multiple students")
    print("3. View grade scale")
    print("4. Exit")
    print("="*50)

def show_grade_scale():
    print("\n" + "-"*50)
    print("GRADING SCALE:")
    print("-"*50)
    print("A+ (95-100): Excellent - Outstanding performance")
    print("A  (90-94):  Excellent - Very Good performance")
    print("B  (80-89):  Good - Above average performance")
    print("C  (70-79):  Average - Satisfactory performance")
    print("D  (60-69):  Below Average - Passing performance")
    print("F  (0-59):   Fail - Needs improvement")
    print("-"*50 + "\n")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '4':
            print("Thank you for using the grade checker. Goodbye!")
            break
        
        elif choice == '1':
            try:
                student_name = input("Enter student name: ")
                score = float(input("Enter student score (0-100): "))
                
                if 0 <= score <= 100:
                    grade = get_grade(score)
                    description = get_grade_description(grade)
                    print(f"\n{'='*50}")
                    print(f"Student: {student_name}")
                    print(f"Score: {score}")
                    print(f"Grade: {grade}")
                    print(f"Description: {description}")
                    print(f"{'='*50}\n")
                else:
                    print("Invalid score! Please enter a score between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter valid data.")
        
        elif choice == '2':
            try:
                num_students = int(input("Enter number of students: "))
                students = []
                
                for i in range(num_students):
                    print(f"\n--- Student {i+1} ---")
                    student_name = input("Enter student name: ")
                    score = float(input("Enter student score (0-100): "))
                    
                    if 0 <= score <= 100:
                        grade = get_grade(score)
                        students.append({
                            'name': student_name,
                            'score': score,
                            'grade': grade
                        })
                    else:
                        print("Invalid score! Skipping this student.")
                
                print(f"\n{'='*50}")
                print("STUDENT GRADES SUMMARY")
                print(f"{'='*50}")
                print(f"{'Name':<20} {'Score':<10} {'Grade':<10}")
                print(f"{'-'*50}")
                
                for student in students:
                    print(f"{student['name']:<20} {student['score']:<10} {student['grade']:<10}")
                
                print(f"{'='*50}\n")
            except ValueError:
                print("Invalid input! Please enter valid data.")
        
        elif choice == '3':
            show_grade_scale()
        
        else:
            print("Invalid choice! Please enter a valid option (1-4).")

if __name__ == "__main__":
    main()
