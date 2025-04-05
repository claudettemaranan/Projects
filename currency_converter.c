#include <stdio.h>
#include <string.h>

float convert_currency(float amount, float exchange_rate) {
    return amount * exchange_rate;
}

int main() {
    char repeat[4];  
    int choice;  

    do {
        float peso_amount;
        const float usd_rate = 0.017752281;
        const float bhd_rate = 0.0066748575;
        const float hkd_rate = 0.13872458;
        const float jpy_rate = 2.6311257;

        printf("\nEnter the amount in Pesos: P");

        while (scanf("%f", &peso_amount) != 1) {
            printf("\nInvalid input. Please enter a numeric value.\n");
            while (getchar() != '\n'); 
            printf("\nEnter the amount in Pesos: P");
        }
         
        printf("\n1. US Dollars\n");
        printf("2. Bahrain Dinar\n");
        printf("3. Hong Kong Dollar\n");
        printf("4. Japanese Yen\n");
        printf("5. Exit\n");

        do {
            printf("\nEnter your choice: ");
            scanf("%d", &choice); 

            if (choice != 1 && choice != 2 && choice != 3 && choice != 4 && choice != 5){
                printf("\nInvalid Input! Please enter a valid choice.\n");
                while(getchar() != '\n');  
            }
        } while (choice != 1 && choice != 2 && choice != 3 && choice != 4 && choice != 5); 


        
        if (choice == 1){
            float usd_amount = convert_currency(peso_amount, usd_rate);
            printf("\nAmount in US Dollar: %.2f\n", usd_amount);
        }
        else if (choice == 2){
            float bhd_amount = convert_currency(peso_amount, bhd_rate);
            printf("Amount in Bahrain Dinar: %.2f\n", bhd_amount);
        }
        else if (choice == 3){
            float hkd_amount = convert_currency(peso_amount, hkd_rate);
            printf("Amount in Hong Kong Dollar: %.2f\n", hkd_amount);
        }
        else if (choice == 4){
            float jpy_amount = convert_currency(peso_amount, jpy_rate);
            printf("Amount in Japanese Yen: %.2f\n", jpy_amount);
        }
        else if (choice == 5){
            break;  
        }

        printf("\nDo you want to run the program again? (yes/no): ");
        scanf("%3s", repeat);  

        while (strcasecmp(repeat, "yes") != 0 && strcasecmp(repeat, "no") != 0) {
            printf("\nInvalid input. Please enter yes or no only.\n");
            while (getchar() != '\n');  
            printf("\nDo you want to run the program again? (yes/no): ");
            scanf("%3s", repeat);
        }

    } while (strcasecmp(repeat, "yes") == 0);  

    printf("\nThank you for using the currency converter!\n");
    return 0;
}
