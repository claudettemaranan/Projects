#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>



bool isLeapYear(int year);

int calculateDayOfWeek(int day, int month, int year);

int main() {
    char input[10];
    int day, month, year;
    char choice;

    do {
        
        bool isValidInput = false;
        do {
            printf("\nEnter the day (1-31): ");
            fgets(input, sizeof(input), stdin);
            if (sscanf(input, "%d", &day) != 1 || day < 1 || day > 31) {
                printf("\nInvalid input. Please enter a numeric value between 1 and 31.\n");
                continue;
            }
            isValidInput = true;
        } while (!isValidInput);

        
        isValidInput = false;
        do {
            printf("\nEnter the month (1-12): ");
            fgets(input, sizeof(input), stdin);
            if (sscanf(input, "%d", &month) != 1 || month < 1 || month > 12) {
                printf("\nInvalid input. Please enter a numeric value between 1 and 12.\n");
                continue;
            }
            isValidInput = true;
        } while (!isValidInput);

        
        isValidInput = false;
        do {
            printf("\nEnter the year (e.g., 2000): ");
            fgets(input, sizeof(input), stdin);
            if (sscanf(input, "%d", &year) != 1 || year < 0) {
                printf("\nInvalid input. Please enter a valid positive numeric value.\n");
                continue;
            }
            isValidInput = true;
        } while (!isValidInput);

        
        int dayOfWeek = calculateDayOfWeek(day, month, year);

        
        const char *days[] = {"Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};
        printf("\nThe day of the week is: %s\n", days[dayOfWeek]);

        
        printf("\nDo you want to run the program again? (y/n): ");
        fgets(input, sizeof(input), stdin);  
        sscanf(input, "%c", &choice);
        while ((getchar()) != '\n');  

    } while (choice == 'y' || choice == 'Y');

    return 0;
}


bool isLeapYear(int year) {
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}


int calculateDayOfWeek(int day, int month, int year) {
    if (month < 3) {
        month += 12;
        year--;
    }
    int y = year % 100;
    int c = year / 100;
    int m = month;
    int d = (day + (26 * (m + 1)) / 10 + y + y / 4 + c / 4 + 5 * c) % 7;
    return d;
}
