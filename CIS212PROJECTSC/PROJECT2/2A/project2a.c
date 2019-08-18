#include <stdio.h>

int main()
{
int i;
int index;
int j;
	for(i = 5; i <= 100 ; i++){
		index = 0;
		for(j = 3; j <= i/2; j++){
			if(i%j == 0){
				index++;
				break;
			}	
		}	
		if(index == 0 && i != 1){
			printf("%d is a prime number\n",i);
		}
			
	}return 0;
}
