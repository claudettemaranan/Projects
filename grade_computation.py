def calculate_final_grade(lab_scores, notebook_score, project_score, practical_exams):
    lab_report_average = sum(lab_scores) / len(lab_scores)
    practical_exam_average = sum(practical_exams) / len(practical_exams)

    lab_grade = lab_report_average * 0.40
    notebook_grade = notebook_score * 0.10
    project_grade = project_score * 0.30
    practical_exam_grade = practical_exam_average * 0.20

    final_grade = lab_grade + notebook_grade + project_grade + practical_exam_grade
    
    return final_grade



def dlsu_grading_scale(final_grade):
    if final_grade > 100:
        return "Error: Total grade cannot exceed 100."
    elif 96 <= final_grade <= 100:
        return "Your DLSU Grade is: 4.0"
    elif 92 <= final_grade < 96:
        return "Your DLSU Grade is: 3.5"
    elif 88 <= final_grade < 92:
        return "Your DLSU Grade is: 3.0"
    elif 83 <= final_grade < 88:
        return "Your DLSU Grade is: 2.5"
    elif 78 <= final_grade < 83:
        return "Your DLSU Grade is: 2.0"
    elif 74 <= final_grade < 78:
        return "Your DLSU Grade is: 1.5"
    elif 70 <= final_grade < 74:
        return "Your DLSU Grade is: 1.0"
    elif final_grade < 70:
        return "Your DLSU Grade is: 0.0"
    else:
        return "Invalid Input!"



def main():
    while True:
        lab_scores = []
        
        for i in range(1, 6):
            while True:
                score = float(input(f"Enter the score for Lab Report {i} (0-100): "))
                if 0 <= score <= 100:
                    lab_scores.append(score)
                    break
                else:
                    print("\nInvalid input. Please enter a score between 0 and 100.\n")

        while True:
            notebook_score = float(input("Enter the score for the Student Notebook (0-100): "))
            if 0 <= notebook_score <= 100:
                break
            else:
                print("\nInvalid input. Please enter a score between 0 and 100.\n")

        while True:
            project_score = float(input("Enter the score for the Project (0-100): "))
            if 0 <= project_score <= 100:
                break
            else:
                print("\nInvalid input. Please enter a score between 0 and 100.\n")

        practical_exams = []
        
        for x in range(1, 3):
            while True:
                exam = float(input(f"Enter the score for Practical Exam {x} (0-100): "))
                if 0 <= exam <= 100:
                    practical_exams.append(exam)
                    break
                else:
                    print("\nInvalid input. Please enter a score between 0 and 100.\n")

        final_grade = calculate_final_grade(lab_scores, notebook_score, project_score, practical_exams)
        dlsu_grade = dlsu_grading_scale(final_grade)

        print(f"\nFinal Grade: {final_grade:.2f}")
        print(dlsu_grade)

        retry = input("\nWould you like to calculate another grade? (yes/no): ").strip().lower()
        if retry != "yes":
            print("\nThank you for using the Grade Calculator!")
            break

main()
