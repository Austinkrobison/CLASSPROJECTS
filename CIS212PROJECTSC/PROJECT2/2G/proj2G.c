#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PIXELS 376000 

typedef struct
{
	unsigned char 	R,	G,	B;
} Pixel;

typedef struct
{
	int width;
	int height;
	Pixel arr[MAX_PIXELS];
} Image;

/*
 * Arguments:
 *   filename: the name of the file to read
 *   img:      a pointer to an Image struct.  You put the data from the
 *             file in this struct
 */

void
ReadImage(char *filename, Image *img)
{
   	 fprintf(stderr, "Reading image \"%s\"\n", filename);

	char magicNum[128];
	int width, height, maxval;
	FILE *f_in = fopen(filename, "r");	
	fscanf(f_in, "%s\n%d %d\n%d\n", magicNum, &width, &height, &maxval);  
	img->height = height;	
	img->width = width;	
	int i;
	Pixel p;
	for(i = 0; i < height * width ; i++){
		fread( &(p.R), 1, 1, f_in);	
		fread( &(p.G), 1, 1, f_in);	
		fread( &(p.B), 1, 1, f_in);	
		img->arr[i] = p;	
	}	  
   
	fclose(f_in); 
	/* where f_in is the name of the input FILE.
     * NOTE: maxval is not needed, but we need to parse it.
     * NOTE: after the fscanf above, the file position indicator will
     * be pointing directly at the pixel data.
     */

    fprintf(stderr, "Done reading image \"%s\"\n", filename);
}


/*
 * Arguments:
 *   filename: the name of the file to write
 *   img:      a pointer to an Image struct.  You put the data from the
 *             file in this struct
 */

void WriteImage(char *filename, Image *img)
{
    fprintf(stderr, "Writing image \"%s\"\n", filename);

	FILE *f_o = fopen(filename, "w");
	fprintf(f_o, "%s\n%d %d\n%d\n", "P6", img->width, img->height, 255);
	int i;
	for(i = 0; i < (img->width * img->height); i++){
		fprintf(f_o, "%c", img->arr[i].R);
		fprintf(f_o, "%c", img->arr[i].G);
		fprintf(f_o, "%c", img->arr[i].B);
	} 
	fclose(f_o);
   /* HINT:
     *  use fprintf to print out the first 4 lines of the file
     *  then use fwrite to print binary data.
     */

    fprintf(stderr, "Done writing image \"%s\"\n", filename);
}

/* 
 * Arguments:
 *    width:  the width of the image
 *    height: the height of the image
 *    row:    the row of the pixel
 *    column: the column of the pixel
 *
 * Returns: the index of the pixel in the image for (column, row)
 */

int GetPixelIndex(int width, int height, int row, int column)
{
    if (column < 0 || column >= width)
    {
        fprintf(stderr, "You asked for a pixel index for column %d, but the only valid values are between 0 and %d\n", column, width-1);
        exit(EXIT_FAILURE);
    }
    if (row < 0 || row >= height)
    {
        fprintf(stderr, "You asked for a pixel index for row %d, but the only valid values are between 0 and %d\n", row, height-1);
        exit(EXIT_FAILURE);
    }
    return row*width + column;
}

/* 
 * Arguments:
 *   input:    an image.  Take this image and replace the diagonal with
 *             a yellow line.
 *   output:   an image.  This should be the image with the yellow line
 *             diagonal.
 */
void YellowDiagonal(Image *input, Image *output1)
{
    fprintf(stderr, "Executing YellowDiagonal\n");
	Image *output = malloc(sizeof(Image));	
	int i;
	int j = 0;
	output->width = 500;
	output->height = 376;	
	for(i = 0; i<(input->width * input->height) ; i++){
		if(i == j + (j  * input->width) ){
			output->arr[i].R = 255;
			output->arr[i].G = 255;
			output->arr[i].B = 0;
			j++;	
		}else{
			output->arr[i].R = input->arr[i].R;	
			output->arr[i].G = input->arr[i].G;	
			output->arr[i].B = input->arr[i].B;	
		} 
	
	}
   
	 /* HINTS: 
     *   You will need to assign values to every data member of the output.
     *   For the output's Pixel array you will need to do a malloc to get
     *   a new array.
     *   Yellow in R/G/B is 255/255/0.
     */

	*output1 = *output;	
	free(output);
    fprintf(stderr, "Done executing YellowDiagonal\n");
}

/* 
 * Arguments:
 *   input1:    an image.  This is the "left image".
 *   input2:    an image.  This is the "right image".
 *   output:    an image.  This is the horizontal combination of input1 and 2.
 */
void LeftRightCombine(Image *input1, Image *input2, Image *output1)
{
	 fprintf(stderr, "Executing LeftRightCombine\n");
	Image *output = malloc(sizeof(Image));	
	output->width = 1000;
	output->height = 376;	

	int i;
	int idx1 = 0;
	int idx2 = 0;	
	int k = 1;	
	for( i = 0 ; i < (1000 * 376) ; i++){
		
		if(i%(input1->width) == 0 && i != 0){
			k++;	
		}	

		if( k % 2 != 0){	
			output->arr[i].R = input1->arr[idx1].R;
			output->arr[i].G = input1->arr[idx1].G;
			output->arr[i].B = input1->arr[idx1].B;
			idx1++; 
				
		} else if( k % 2 == 0){
			output->arr[i].R = input2->arr[idx2].R;
			output->arr[i].G = input2->arr[idx2].G;
			output->arr[i].B = input2->arr[idx2].B;
			idx2++;
				
		}
      	}
    /* HINTS: 
     *   You will need to assign values to every data member of the output.
     *   For the output's Pixel array you will need to do a malloc to get
     *   a new array.
     *   The output's Pixel array will be larger than either of the inputs.
     *   IMPORTANT: the pixel index for an output pixel will be different
     *     than the pixel index for either of the inputs ... you will need
     *     to call GetPixelIndex multiple times.
     */
	*output1 = *output;
	free(output);	
	fprintf(stderr, "Done executing LeftRightCombine\n");
}

void
VerifyInput()
{
    FILE *f_in = fopen("2G_input.pnm", "r");
    if (f_in == NULL)
    {
        fprintf(stderr, "Cannot open 2G_input.pnm for reading.\n");
        exit(EXIT_FAILURE);
    }
    fclose(f_in);

    FILE *f_out = fopen("2G_output.pnm", "w");
    if (f_out == NULL)
    {
        fprintf(stderr, "Cannot open 2G_output.pnm for writing.\n");
        exit(EXIT_FAILURE);
    }
    fclose(f_out);
}

int main(int argc, char *argv[])
{
    VerifyInput();

    Image source_image;
    
    Image yellow_diagonal;
    Image left_right;

    ReadImage("2G_input.pnm", &source_image);
    WriteImage("output_of_read.pnm", &source_image);

    YellowDiagonal(&source_image, &yellow_diagonal);
    WriteImage("yellow_diagonal.pnm", &yellow_diagonal);

    LeftRightCombine(&source_image, &yellow_diagonal, &left_right);
    WriteImage("2G_output.pnm", &left_right);
    
    return(0);
}
