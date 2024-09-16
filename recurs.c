#include <stdio.h>
#include <string.h>

int main(void){
    char name[] ="";

/*     while(strlen(name) == 0){
        printf("what is your name? ");
        scanf("%s", name);
    } */
    while (1)
    {
        printf("what is your name? ");
        scanf("%s", name);
        if (strlen(name) != 0){
            break;
        }
    }
    
    printf("your name is %s", name);
}