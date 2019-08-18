#include <stdio.h>
#include <stdlib.h>
int main(int argc, char* argv []){
	int i;
	FILE *f_in = fopen(argv[1], "r");
	FILE *f_out = fopen(argv[2], "w");	
	char buffer[25];	
	fseek(f_in,0,SEEK_SET);	
	for(i = 0; i < 25; i++){
		buffer[i] = ftell(f_in);	
		fread(buffer, 1 , 1, f_in);
		if((i %5 ) == 4){
			fseek(f_in, 5, SEEK_CUR); 
		}
		fprintf(f_out, "%d\n", buffer[i]);	
	}
	fclose(f_in);
	fclose(f_out); 
	return 0;
} 
