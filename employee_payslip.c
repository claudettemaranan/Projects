#include <stdio.h>
#include <string.h>

int main() {
    char repeat[4];

    do {
        int employee_id;
        float rate_per_hour, hours_worked, gross_pay, tax, sss, philhealth, pagibig, total_deductions, net_pay;

        printf("\nEnter employee's ID number: ");

        while (scanf("%d", &employee_id) != 1) {
            printf("\nInvalid input. Please enter a numeric value.\n");
            while (getchar() != '\n');
            printf("\nEnter employee's ID number: ");
        }

        printf("\nEnter rate per hour: ");

        while (scanf("%f", &rate_per_hour) != 1) {
            printf("\nInvalid input. Please enter a numeric value.\n");
            while (getchar() != '\n');
            printf("\nEnter rate per hour: ");
        }

        printf("\nEnter number of hours worked for two weeks: ");

        while (scanf("%f", &hours_worked) != 1) {
            printf("\nInvalid input. Please enter a numeric value.\n");
            while (getchar() != '\n');
            printf("\nEnter number of hours worked for two weeks: ");
        }

        gross_pay = rate_per_hour * hours_worked;

        tax = 0.2 * gross_pay;
        sss = 0.05 * gross_pay;
        philhealth = 150;
        pagibig = 150;

        total_deductions = tax + sss + philhealth + pagibig;

        net_pay = gross_pay - total_deductions;

        printf("\n--- Employee Payroll Summary ---\n");
        printf("Employee ID: %d\n", employee_id);
        printf("Gross Pay (2 weeks): %.2f\n", gross_pay);
        printf("Total Deductions: %.2f\n", total_deductions);
        printf("Net Pay: %.2f\n", net_pay);

        printf("\nDo you want to run the program again? (yes/no): ");
        scanf("%3s", repeat);  

        while (strcasecmp(repeat, "yes") != 0 && strcasecmp(repeat, "no") != 0) {
            printf("\nInvalid input. Please enter yes or no only.\n");
            while (getchar() != '\n');  
            printf("\nDo you want to run the program again? (yes/no): ");
            scanf("%3s", repeat);
        }

    } while (strcasecmp(repeat, "yes") == 0);

    printf("Thank you for using the payroll calculator!\n");

    return 0;
}