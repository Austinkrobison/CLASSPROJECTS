#include <stdio.h>
#include <stdlib.h>

int my_strlen(char *s){
	int count =0;
	while(*s != '\0'){
		s++;
		count++;
	}
	return(count);
}

int ParseNum(char *num){
	int sum = 0;	
	int Nsign = 0;
	int strLen = my_strlen(num);
	if(num[0] == '-')
		Nsign = 1;
	if(strLen > 10+Nsign){
		printf("ERROR: number has 10 or more digits\n");
		exit(EXIT_FAILURE);
	}	
	for( int n = 0 + Nsign; n < 10 + Nsign; n++){
		char digit = num[n];
		if(digit == '\0')
			break;
		if(digit < '0' || digit > '9'){
			printf("ERROR: number has character that is outside 0-9\n");
			exit(EXIT_FAILURE);
		}
		int m = n+1;
		char nextdigit = num[m];
		int ndint = digit - '0';
		sum += ndint;	
		if(nextdigit != '\0')
			sum *=10;
	}
	if(Nsign == 1)
		sum *= -1;	
	return(sum);	
}

int main(int argc, char *argv[])
{
    if (argc != 4)
    {
        printf("Usage: %s <integer> <+ or -> <integer>", argv[0]);
        exit(EXIT_FAILURE);
    }

    char *number1 = argv[1];
    char *operation = argv[2];
    char *number2 = argv[3];
	int sum1 = ParseNum(number1);	
	int sum2 = ParseNum(number2);
	int RetVal;	

	if( operation[1] != '\0'){
		printf("ERROR: operation may only be + or -\n");	
		exit(EXIT_FAILURE);
	}else if(operation[0] == '+'){
		RetVal = sum1 + sum2;	
	}else if(operation[0] == '-'){
		RetVal = sum1 - sum2;
	}else{ 
		printf("ERROR: operation may only be + or -\n");
		exit(EXIT_FAILURE);
	}
	printf("%d\n", RetVal);
	
}

