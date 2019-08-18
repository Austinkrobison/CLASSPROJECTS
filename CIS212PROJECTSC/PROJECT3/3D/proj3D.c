/*
 * I believe I have completed:
 *  Map based on linked lists: yes
 *  Double hashing: yes
 *  Performance study: yes 
 */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
typedef struct
{
    char    *symbol;
    char    *name;
    float    lastSale;
    float    marketCap;
    int      IPOyear;
} Company;

void PrintCompany(Company *c)
{
    printf("%s:\n", c->name);
    printf("\tSymbol: %s\n", c->symbol);
    /* .2f: only print two digits after the period. */
    printf("\tLast Sale: %.2f\n", c->lastSale);
    printf("\tMarket Capitalization: %.2f\n", c->marketCap);
    printf("\tYear of Initial Public Offering: %d\n", c->IPOyear);
}

void ReadFile(const char *filename, Company **companies_rv, int *numCompanies_rv)
{
    int  i, j;

    if (filename == NULL)
    {
        fprintf(stderr, "No filename specified!\n");
        exit(EXIT_FAILURE);
    }
    FILE *f_in = fopen(filename, "r");
    if (f_in == NULL)
    {
        fprintf(stderr, "Unable to open file \"%s\"\n", filename);
        exit(EXIT_FAILURE);
    }

    fseek(f_in, 0, SEEK_END);
    int numChars = ftell(f_in);
    // printf("The number of characters is %d\n", numChars);
    fseek(f_in, 0, SEEK_SET);

    char *file_contents = malloc(sizeof(char)*numChars);
    fread(file_contents, sizeof(char), numChars, f_in);
    fclose(f_in);
    /* Note: the memory for this array is used to populate
     * the fields of the companies.  If it is freed, then
     * the company structs all become invalid.  For the
     * context of this program, this array should not be 
     * freed. */

    // Find out how many lines there are
    int numLines = 0;
    for (i = 0 ; i < numChars ; i++)
        if (file_contents[i] == '\n')
            numLines++;
    // printf("Number of lines is %d\n", numLines);

    int      numCompanies = numLines-1; // first line is header info 
    Company *companies    = malloc(sizeof(Company)*numCompanies);

    /* strtok will parse the file_contents array.  
     * The first time we call it, it will replace every '"' with '\0'.
     * It will also return the first word before a 
     */
    int numColumns = 9;
    int numberOfQuotesPerColumn = 2;
    strtok(file_contents, "\"");
    for (i = 0 ; i < numberOfQuotesPerColumn*numColumns-1 ; i++)
         strtok(NULL, "\"");
    for (i = 0 ; i < numCompanies ; i++)
    {
         companies[i].symbol = strtok(NULL, "\"");
         strtok(NULL, "\"");
         companies[i].name = strtok(NULL, "\"");
         strtok(NULL, "\"");
         companies[i].lastSale = atof(strtok(NULL, "\""));
         strtok(NULL, "\"");
         companies[i].marketCap = atof(strtok(NULL, "\""));
         strtok(NULL, "\""); 

         /* Skip ADR TSO */
         strtok(NULL, "\"");
         strtok(NULL, "\"");

         companies[i].IPOyear = atoi(strtok(NULL, "\""));
         strtok(NULL, "\"");

         /* Skip Sector, Industry, Summary Quote */
         for (j = 0 ; j < 6 ; j++)
             strtok(NULL, "\"");

         //PrintCompany(companies+i);
    }

    /* Set parameters to have output values */
    *companies_rv    = companies;
    *numCompanies_rv = numCompanies;
}

int hash(char *name, int array_size)
{
    int hashval = 0;
    char *p = name;
    while (*p != '\0')
    {
        hashval = 31*hashval + *p;
        p++;
    }

    return hashval%array_size;
}

/* REFERENCE: www.cse.yorku.ca/~oz/hash.html djb2 by Dan Bernstein */
int  hash2(char *str){
	int hash = 5381;
	int c;
	while(c = *str++){
		hash = ((hash << 5) + hash) +c;
	}
	return(hash);
}

int doublehash(char *str, int arrlen){
	int val = (hash(str, arrlen) + arrlen * hash2(str)) % arrlen;
	/*fprintf(stderr, "%s, stored at  %d\n", str ,val);*/ 
	return(val);
}

typedef struct 
{
    int         numElements;
    char      **keys;
    Company    *companies;
} MapBasedOnHashTable;

void InitializeMapBasedOnHashTable(MapBasedOnHashTable *map, int numElements)
{
    map->numElements = numElements;
    map->keys = malloc(sizeof(char *)*numElements);
    map->companies = malloc(sizeof(Company)*numElements);
    for (int i = 0 ; i < numElements ; i++)
        map->keys[i] = NULL;
}

void StoreTo_MapBasedOnHashTable(MapBasedOnHashTable *map, Company *c)
{
    int hashval = doublehash(c->symbol, map->numElements);
    for (int i = 0 ; i < map->numElements ; i++)
    {
        int idx = (hashval+i)%(map->numElements);
        if (idx < 0) idx+= map->numElements;
        if (map->keys[idx] == NULL)
        {
            map->keys[idx]      = c->symbol;
            map->companies[idx] = *c;
            return;
        }
    }
}

Company *
FetchFrom_MapBasedOnHashTable(MapBasedOnHashTable *map, char *key)
{
    int hashval = doublehash(key, map->numElements);
    for (int i = 0 ; i < map->numElements ; i++)
    {
        int idx = (hashval+i)%(map->numElements);
        if (idx < 0) idx+= map->numElements;
        if (map->keys[idx] == NULL)
        {
            return NULL;
        }

        if (strcmp(map->keys[idx], key) == 0)
        {
            return &(map->companies[idx]);
        }
    }
    
    return NULL;
}

void FetchAndPrint(MapBasedOnHashTable *mfht, char *key)
{
    Company *c = FetchFrom_MapBasedOnHashTable(mfht, key);
    if (c == NULL)
    {
        printf("Key %s has no corresponding company\n", key);
    }
    else
    {
        PrintCompany(c);
    }

}
struct ll_node{
	struct ll_node *next;
	char* key;	
	int value;
};

struct ll_node * ll_insert(int v, char *k, struct ll_node *cur_head){
	struct ll_node *rv = malloc(sizeof(struct ll_node));
	rv->value = v;
	rv->key = k;	
	rv->next = cur_head;
	return(rv);
}
char * fetchfromll(struct ll_node *node, char* sym){
	int i;
	int TBF = doublehash(sym, strlen(sym));	
	struct ll_node * nn =  node->next;	
	while(nn != NULL){
		if(TBF == node->value){
			return(sym);
		} 
		nn = node->next;		
	}
	fprintf(stderr, "Key %s has no corresponding company/n", sym);
	return("NULL");	
}
int main(int argc, char *argv[])
{
    Company *companies = NULL;
    int      numCompanies;
    ReadFile(argv[1], &companies, &numCompanies);
    MapBasedOnHashTable mfht;
    printf("\nnum companies is %d\n", numCompanies);
    InitializeMapBasedOnHashTable(&mfht, numCompanies*2);
   	int i; 

	struct timeval startTime;
	gettimeofday(&startTime, 0 );
    
    for (i = 0 ; i < numCompanies ; i++)
    {
        StoreTo_MapBasedOnHashTable(&mfht, companies+i);
    }
	struct timeval endTime;
	gettimeofday(&endTime, 0);
	double time = (double)(endTime.tv_sec - startTime.tv_sec) + (double)(endTime.tv_usec - startTime.tv_usec) / 1000000;
	fprintf(stderr, "\ntook %g seconds to populate map based on hashtable with %d values\n", time, numCompanies);

	gettimeofday(&startTime, 0 );
	struct ll_node *cur_head = NULL;	
/* -------------------populating map based on linked list---------------------------- */	
	for(i = 0; i < numCompanies; i++){
		cur_head = ll_insert(doublehash(companies[i].symbol, strlen(companies[i].symbol)), companies[i].symbol, cur_head);	
	}
	gettimeofday(&endTime, 0);
	double tim = (double)(endTime.tv_sec - startTime.tv_sec) + (double)(endTime.tv_usec - startTime.tv_usec) / 1000000;
	fprintf(stderr, "took %g seconds to populate map based on linked list with %d values\n", tim, numCompanies);

	gettimeofday(&startTime, 0 );
/* --------------------fetching from mapbasedonhashtable -------*/								
	FetchAndPrint(&mfht, companies[numCompanies-1].symbol);

	gettimeofday(&endTime, 0);
	double fetchtime = (double)(endTime.tv_sec - startTime.tv_sec) + (double)(endTime.tv_usec - startTime.tv_usec) / 1000000;
	fprintf(stderr, "took %lf seconds to fetch 3000th value of map based on hash table\n", fetchtime);

/* 
   FetchAndPrint(&mfht, "Z");
    FetchAndPrint(&mfht, "ZIOP");
    FetchAndPrint(&mfht, "ZIOQ");
    FetchAndPrint(&mfht, "YIOQ");
    FetchAndPrint(&mfht, "QIOQ");
    FetchAndPrint(&mfht, "WIOQ");
    FetchAndPrint(&mfht, "XIOQ");
    FetchAndPrint(&mfht, "TIOQ");
    FetchAndPrint(&mfht, "UIOQ");
    FetchAndPrint(&mfht, "VIOQ");
*/   
	gettimeofday(&startTime, 0 );
/* ---- fetching from map based on linked list ---*/	
	printf("found %s\n", fetchfromll(cur_head, companies[numCompanies-1].symbol));
	gettimeofday(&endTime, 0);
	double fetchtime2 = (double)(endTime.tv_sec - startTime.tv_sec) + (double)(endTime.tv_usec - startTime.tv_usec) / 1000000;
	fprintf(stderr, "took %lf seconds to fetch 3000th value of map based on linked list\n", fetchtime2);

 
}

/* YOUR PERFORMANCE STUDY WRITEUP GOES HERE:
	The second hash function (hash2()) that I chose is cited above the section of code i used, then i used the 	
	provided hash function with hash2 for my double hash function to reduce collisions.	
	As far as storing data goes, every test that I make the mapbasedonhastable is faster, this is expected 
	because there is an extra data member for the link for every company that is stored. 
	however, when the times for linked list fetching are compared to the hashtable fetching you can really notice how much faster
	the linked list is for fetching. 
*/
