
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define QUEUE_SIZE 10

typedef struct
{
	int front, back;
		
	char* strings[100];

} Queue;
void Enqueue(Queue *Q, char* Entry){
	if( Q->back - Q->front >= QUEUE_SIZE){
		fprintf(stderr, "QUEUE FULL");
	}else{	
		Q->strings[Q->back] = Entry;
		/* fprintf(stderr, "added %s to the queue\n", Entry);*/	
		Q->back += 1;
	}
}
char* Dequeue(Queue *Q){
	return(Q->strings[Q->front++]);	
}
void InitializeQueue(Queue *Q){
	Q->front = 0;
	Q->back = 0;	

}

void
PrintQueue(Queue *q)
{
    int i;
    printf("Printing queue %p\n", q);
    printf("\tThe index for the front of the queue is %d\n", q->front);
    printf("\tThe index for the back of the queue is %d\n", q->back);
    if (q->front == q->back)
    {
        printf("\tThe queue is empty.\n");
        return;
    }
    int back = q->back;
    if (q->back < q->front)
    {
        // wrapped around, so modify indexing 
        
    }

    for (i = q->front ; i < back ; i++)
    {
        printf("\t\tEntry[%d] = \"%s\"\n", i%QUEUE_SIZE, q->strings[i%QUEUE_SIZE]);
    }
}

void
PrettyPrintQueue(Queue *q, char *type)
{
    if (q->front >= q->back)
    {
        printf("No unmatched entries for %s\n", type);
    }
    else
    {
        char *s;
        printf("Unmatched %s:\n", type);
        while (q->front < q->back)
        {
		printf("\t%s\n", Dequeue(q));
	}
    }
}

char *NewString(char *s)
{
    int len = strlen(s);
    char *rv = malloc(len);
    strcpy(rv, s);
    rv[len-1] = '\0'; /* take out newline */
    return rv;
}
int main(int argc, char* argv [])
{
/***  STEP #1: Test your queue code.  ***/
/*
    Queue q;
    InitializeQueue(&q);
    PrintQueue(&q);
    Enqueue(&q, "hello");
    PrintQueue(&q);
    Enqueue(&q, "world");
    PrintQueue(&q);
    printf("Dequeue: %s\n", Dequeue(&q));
    PrintQueue(&q);
*/

/* Gives this output (with different pointers):
Printing queue 0x7fff5e6878a8
	The index for the front of the queue is 0
	The index for the back of the queue is 0
	The queue is empty.
Printing queue 0x7fff5e6878a8
	The index for the front of the queue is 0
	The index for the back of the queue is 1
		Entry[0] = "hello"
Printing queue 0x7fff5e6878a8
	The index for the front of the queue is 0
	The index for the back of the queue is 2
		Entry[0] = "hello"
		Entry[1] = "world"
HDequeue: hello
Printing queue 0x7fff5e6878a8
	The index for the front of the queue is 1
	The index for the back of the queue is 2
		Entry[1] = "world"
 */

/*** STEP #2: read in from the input file (argc/argv stuff). 
     NewString is likely helpful here.
 ***/
	FILE *f_in = fopen(argv[1], "r");
	char line[256];
	int linenum =0;	
	int Hcnt = 0;	
	Queue H, FD, FR, MD, MR;	
	InitializeQueue(&H);	
	InitializeQueue(&FD);	
	InitializeQueue(&FR);	
	InitializeQueue(&MD);	
	InitializeQueue(&MR);	
	while(fgets(line, 256, f_in) != NULL){
		if(line[0] == 'H'){
			Enqueue(&H, NewString(line+2));
			Hcnt++;	
		}else if(line[0] == 'D'){
			if(line[2] == 'F'){
				Enqueue(&FD, NewString(line+4));	
			}else if(line[2] == 'M'){
				Enqueue(&MD, NewString(line+4));
			}
		}else if(line[0] == 'R'){
			if(line[2] == 'F'){
				Enqueue(&FR, NewString(line+4));	
			}else if(line[2] == 'M'){
				Enqueue(&MR, NewString(line+4));
			}
		}else{
			fprintf(stderr, "Input file error, now exiting\n");
			exit(EXIT_FAILURE);	
		}	
		
		if(Hcnt > 0){
    			if(FD.strings[FD.front] != FD.strings[FD.back] && FR.strings[FR.front] != FR.strings[FR.back]){
				Hcnt--;	
				printf("MATCH: %s donates to %s at hospital %s\n", Dequeue(&FD),Dequeue(&FR), Dequeue(&H));
			}	

    			else if(MD.strings[MD.front] != MD.strings[MD.back] && MR.strings[MR.front] != MR.strings[MR.back]){
				Hcnt--;	
				printf("MATCH: %s donates to %s at hospital %s\n", Dequeue(&MD),Dequeue(&MR), Dequeue(&H));

			}	
		
		}
	}	
	PrettyPrintQueue(&FD, "female donors");
	PrettyPrintQueue(&FR, "female recipients");
	PrettyPrintQueue(&MD, "male donors");
	PrettyPrintQueue(&MR, "male recipients");
	PrettyPrintQueue(&H, "hospitals");

/*** STEP #3: *after* your queue code works and *after* you can read the file, 
     implement the prompt ***/
/* Here are some helpful lines of code:
 *
 *  My print statement for a match:
 *
    printf("MATCH: %s donates to %s at hospital %s\n", donor, recip, hosp);
 *
 *
 *  My print statements for the contents of the queues at the end:
 *
    PrettyPrintQueue(&female_donors, "female donors");
    PrettyPrintQueue(&female_recipients, "female recipients");
    PrettyPrintQueue(&male_donors, "male donors");
    PrettyPrintQueue(&male_recipients, "male recipients");
    PrettyPrintQueue(&hospitals, "hospitals");
 *
 */
}
