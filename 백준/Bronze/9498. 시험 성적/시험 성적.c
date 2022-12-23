#include <stdio.h>

int main()
{
    int a;
    scanf("%d",&a);
    if((a<=101)&&(a>=90)) printf("A");
    else if((a<90)&&(a>79)) printf("B");
    else if((a<80)&&(a>69)) printf("C");
    else if((a<70)&&(a>59)) printf("D");
    else printf("F");
    return 0;
}