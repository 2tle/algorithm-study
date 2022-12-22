#include <stdio.h>
#include <stdlib.h>

int arr[1003];
int qS(const void* a,const void* b)
{
    int c1 = *(int *)a;
    int c2 = *(int *)b;
    return c1-c2;
}
int main()
{
    int x;
    scanf("%d",&x);
    for(int i = 0;i<x;i++)
    {
        scanf("%d",&arr[i]);
    }
    qsort(&arr, x, sizeof(arr[0]), qS);
    int bestScore = arr[x-1];
    float f = 0.0;
    for(int i =0;i<x;i++)
    {
        f = f+((float)arr[i]/(float)bestScore)*(float)100;
    }
    printf("%f",f/x);
    return 0;
    
    
}