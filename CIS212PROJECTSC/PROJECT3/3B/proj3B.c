#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_ARGS 100

typedef struct{
	int Count;
	int arr[MAX_ARGS];
} Stack;
void Initialize(Stack *s){
	s->Count = 0;
}
void Push(Stack *s, int X){
	s->arr[s->Count] = X;
	s->Count += 1;	
}
int Pop(Stack *s){
	int X = s->arr[--(s->Count)];	
	return(X);
}

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

void main(int argc, char *argv[])
{
	int i, x;
	Stack F;	
	Stack *s = &F;	
	Initialize(s);	
	for( i = 1; i < argc; i++){
		char *num = argv[i];	
		if(num[0] > '0' && num[0] < '9'){
			x = ParseNum(num);		
			Push(s, x );
		} else if(num[0] == 'x'){
			int TBP = Pop(s) * Pop(s);	
			Push(s, TBP);		
		} else if(num[0] == '+'){
			int TBP = Pop(s) + Pop(s);
			Push(s, TBP);
		} else if(num[0] == '-'){
			int A = Pop(s);
			int B = Pop(s);
			Push(s, B - A);	
		}	
	}
		
	printf("The total is %d\n", Pop(s));
}
