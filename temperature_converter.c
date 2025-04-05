#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    char unit1, unit2;
    float temp;
    char repeat[4];  

    do {    
        do {
            printf("\nDo you want to convert the temperature to Celsius (C), Fahrenheit (F), or Kelvin (K)? ");
            scanf(" %c", &unit1);
            unit1 = toupper(unit1);
            
            if (unit1 != 'C' && unit1 != 'F' && unit1 != 'K') {
                printf("\nInvalid Input! Please enter C, F, or K.\n");
                while (getchar() != '\n'); 
            }
        } while (unit1 != 'C' && unit1 != 'F' && unit1 != 'K');


        
        if (unit1 == 'C') {
            do {
                printf("\nAre you converting from Fahrenheit (F) or Kelvin (K)? ");
                scanf("%c", &unit2);
                unit2 = toupper(unit2);

                if (unit2 != 'F' && unit2 != 'K') {
                    printf("\nInvalid Input! Please enter F or K.\n");
                    while (getchar() != '\n');
                }
            } while (unit2 != 'F' && unit2 != 'K');

            if (unit2 == 'F') {
                printf("\nEnter temperature in Fahrenheit: ");
                scanf("%f", &temp);
                temp = ((temp - 32) * 5) / 9;
                printf("\nTemperature in Celsius: %.1f°C", temp);
            } else if (unit2 == 'K') { 
                printf("\nEnter temperature in Kelvin: ");
                scanf("%f", &temp);
                temp = temp - 273.15;  
                printf("\nTemperature in Celsius: %.1f°C", temp);
            }
        } 
        else if (unit1 == 'F') {
            do {
                printf("\nAre you converting from Celsius (C) or Kelvin (K)? ");
                scanf(" %c", &unit2);
                unit2 = toupper(unit2);

                if (unit2 != 'C' && unit2 != 'K') {
                    printf("\nInvalid Input! Please enter C or K.\n");
                    while (getchar() != '\n');
                }
            } while (unit2 != 'C' && unit2 != 'K');

            if (unit2 == 'C') {  
                printf("\nEnter temperature in Celsius: ");
                scanf("%f", &temp);
                temp = (temp * 9 / 5) + 32;
                printf("\nTemperature in Fahrenheit: %.1f°F", temp);
            } else if (unit2 == 'K') {
                printf("\nEnter temperature in Kelvin: ");
                scanf("%f", &temp);
                temp = ((temp - 273.15) * 9 / 5) + 32;  
                printf("\nTemperature in Fahrenheit: %.1f°F", temp);
            }
        } 
        else if (unit1 == 'K') {
            do {
                printf("\nAre you converting from Celsius (C) or Fahrenheit (F)? ");
                scanf(" %c", &unit2);
                unit2 = toupper(unit2);

                if (unit2 != 'C' && unit2 != 'F') {
                    printf("\nInvalid Input! Please enter C or F.\n");
                    while (getchar() != '\n');
                }
            } while (unit2 != 'C' && unit2 != 'F');

            if (unit2 == 'C') {
                printf("\nEnter temperature in Celsius: ");
                scanf("%f", &temp);
                temp = temp + 273.15;  
                printf("\nTemperature in Kelvin: %.1fK", temp);
            } else {
                printf("\nEnter temperature in Fahrenheit: ");
                scanf("%f", &temp);
                temp = ((temp - 32) * 5 / 9) + 273.15;  
                printf("\nTemperature in Kelvin: %.1fK", temp);
            }
        }



        do {
            printf("\n\nDo you want to convert another? (yes/no): ");
            scanf("%3s", repeat);
            
            for (int i = 0; repeat[i]; i++) {
                repeat[i] = tolower(repeat[i]);
            }

            if (strcmp(repeat, "yes") != 0 && strcmp(repeat, "no") != 0) {
                printf("\nInvalid input. Please enter yes or no only.\n");
                while (getchar() != '\n'); 
            }
        } while (strcmp(repeat, "yes") != 0 && strcmp(repeat, "no") != 0);
    } while (strcmp(repeat, "yes") == 0);  

    return 0;
}
