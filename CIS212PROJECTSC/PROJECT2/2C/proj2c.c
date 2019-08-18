#include <stdio.h>
#include <stdlib.h>

/* NOTE:
 * - you may not use atoi
 * - you may not use *any* built-in functions -- strlen, strcpy, etc.
 * - you may assume all integers have <10 digits
 */

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
	int sum1 = 0;	
	int sum2 = 0;
	int RetVal;	
	for(int i = 0; i < 10; i++){
		char digit = number1[i];
		int j = i+1;	
		char ndigit = number1[j];
		int dint = digit - '0';	
		if( digit == '\0')
			break;
		sum1 += dint;	
		if(ndigit != '\0')
			sum1 *= 10;	
	}
  	for( int n =0; n < 10; n++){
		char digit1 = number2[n];
		int m = n+1;
		char nextdigit = number2[m];
		int ndint = digit1 - '0';
		if( digit1 == '\0')
			break;
		sum2 += ndint;	
		if(nextdigit != '\0')
			sum2 *=10;

	} 
	if(operation[0] == '+')
		RetVal = sum1 + sum2;	
	if(operation[0] == '-')
		RetVal = sum1 - sum2;
	printf("%d\n", RetVal);


	
	 /* Turn number1 into an integer.  You will need to do this by
     * looking at the character string one character at a time, and multiplying
     * by 10 as you go.
     * For example: if the string is "214", then I would start by finding the
     * '2'.  I would think (for the time being) the number is 2.  When I go
     * to the next character, I would see the "1".  I would then make the 
     * number 21, by multiplying my previous number (2) by 10 and adding the
     * current number (1) ... 2*10+1 = 21.
     * The next number is 4.  Again, take the previous number (21) times 10
     * and add the current number (4).  This makes 214.
     * The next character is the NULL character.  So we are done parsing the
     * string.  And stop at 214.
     * TRICK #1! --->
     *    char digit = '5';
     *    int digit_as_number = digit - '0'; <--- gives you 5.
     * TRICK #2! --->
     *    when you encounter a '\0', then use break to terminate the loop
     *    right then.
     */

    /* Now figure out which operation to do: plus or minus.
     * You will do this by inspecting the variable named "operation". */

    /* Now turn number2 into an integer. */
 
    /* Perform the operation and print the result */
}
