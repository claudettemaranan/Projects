#include <stdio.h>
#include <string.h>

float calculate_final_grade(float lab_average, float project_grade, float practical_exam_average);
void print_grade(float total_grade);

int main() {
    char repeat[4];  

    do {
        float lab_grades[3];  
        float notebook_grade, project_grade;
        float practical_exams[2];  

        for (int i = 0; i < 3; i++) {
            while (1) {
                printf("Enter the grade for Lab Report %d (0-100): ", i + 1);
                scanf("%f", &lab_grades[i]);
                if (lab_grades[i] >= 0 && lab_grades[i] <= 100) {
                    break;
                } else {
                    printf("\nInvalid input. Please enter a grade between 0 and 100.\n");
                }
            }
        }

        while (1) {
            printf("Enter the grade for the Student Notebook (0-100): ");
            scanf("%f", &notebook_grade);
            if (notebook_grade >= 0 && notebook_grade <= 100) {
                break;
            } else {
                printf("\nInvalid input. Please enter a grade between 0 and 100.\n");
            }
        }

        while (1) {
            printf("Enter the grade for the Project (0-100): ");
            scanf("%f", &project_grade);
            if (project_grade >= 0 && project_grade <= 100) {
                break;
            } else {
                printf("\nInvalid input. Please enter a grade between 0 and 100.\n");
            }
        }

        for (int i = 0; i < 2; i++) {
            while (1) {
                printf("Enter the grade for Practical Exam %d (0-100): ", i + 1);
                scanf("%f", &practical_exams[i]);
                if (practical_exams[i] >= 0 && practical_exams[i] <= 100) {
                    break;
                } else {
                    printf("\nInvalid input. Please enter a grade between 0 and 100.\n");
                }
            }
        }

        float lab_average = (lab_grades[0] + lab_grades[1] + lab_grades[2]) / 3.0;
        float practical_exam_average = (practical_exams[0] + practical_exams[1]) / 2.0;

        float total_grade = calculate_final_grade(lab_average, project_grade, practical_exam_average);

        printf("\nTotal Grade: %.2f\n", total_grade);
        print_grade(total_grade);

        printf("\nDo you want to run the program again? (yes/no): ");
        scanf("%3s", repeat);  
        while (getchar() != '\n'); 

        while (strcasecmp(repeat, "yes") != 0 && strcasecmp(repeat, "no") != 0) {
            printf("\nInvalid input. Please enter yes or no only.\n");
            printf("\nDo you want to run the program again? (yes/no): ");
            scanf("%3s", repeat);
            while (getchar() != '\n');  
        }

    } while (strcasecmp(repeat, "yes") == 0); 

    return 0;
}


float calculate_final_grade(float lab_average, float project_grade, float practical_exam_average) {
    float lab_score = lab_average * 0.40;
    float project_score = project_grade * 0.30;
    float practical_exam_score = practical_exam_average * 0.30;

    return lab_score + project_score + practical_exam_score;
}


void print_grade(float total_grade) {
    if (total_grade >= 96) {
        printf("Your Grade is: 4.0\n");
    } else if (total_grade >= 92) {
        printf("Your Grade is: 3.5\n");
    } else if (total_grade >= 88) {
        printf("Your Grade is: 3.0\n");
    } else if (total_grade >= 83) {
        printf("Your Grade is: 2.5\n");
    } else if (total_grade >= 78) {
        printf("Your Grade is: 2.0\n");
    } else if (total_grade >= 74) {
        printf("Your Grade is: 1.5\n");
    } else if (total_grade >= 70) {
        printf("Your Grade is: 1.0\n");
    } else {
        printf("Your Grade is: 0.0\n");
    }
}