#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <algorithm>
#include <cmath>

int cmp(int a, int b) {
	return a < b;
}

int arr[1000010];
int main() {
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}
	std::sort(arr, arr + N, cmp);
	for (int i = N-1; i >= 0; i--) {
		printf("%d ", arr[i]);
	}
	return 0;
	
}