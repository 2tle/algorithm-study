#include <stdio.h>
int arr[105];
int F(int a, int b, int k){
	if(arr[a*10+b] != 0) {
		return k - arr[a*10+b];
	}
	arr[a*10+b] = k;
	return F(b,(a+b)%10,k+1);
}
int main(void)
{
	int count = 0;
	int ten = 0;
	int one = 0;
	int n = 0;
	scanf("%d",&n);
	ten = n/10;
	one = n%10;
	printf("%d",F(ten,one,count));
	return 0;
}
