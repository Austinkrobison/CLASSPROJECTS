#include <stdio.h>
#include <stdlib.h>
typedef struct{
	double rminX, rminY, rmaxX, rmaxY;
} Rectangle;
typedef struct{
	double tminY, tminX, tmaxX, tmaxY;
}Triangle;

typedef struct{
	double radius, centerX, centerY;
} Circle;

typedef struct{
	void* self;
	void (*GetBoundingBox)(void* , void*);	
	double (*GetArea)(void*);
} Shape;
 
double GetCircleArea(void *C)
{
	Circle *X = C;	
	return(X->radius * X-> radius *3.14159);
};
double GetRectangleArea(void *R)
{
	Rectangle *X = R;	
	return(  ((X->rmaxX) - (X->rminX)) * ((X->rmaxY) - (X->rminY))  ); 
};
double GetTriangleArea(void *T)
{
	Triangle *X = T;	
	return( (((X->tmaxY) - (X->tminY)) /2) *((X->tmaxX) - (X->tminX)) );  
};
void GetCircleBoundingBox(void *D, void *K)
{
	Circle *X = D;
	double *N = K;	
	N[0] = (X->centerX)-(X->radius);
	N[1] = (X->centerX)+(X->radius);
	N[2] = (X->centerY)-(X->radius);
	N[3] = (X->centerY)+(X->radius);
};
void GetRectangleBoundingBox(void * D, void *K)
{
	Rectangle *X = D;
	double *N = K;
	N[0] = (X->rminX);
	N[1] = (X->rmaxX);
	N[2] = (X->rminY);
	N[3] = (X->rmaxY);
};
void GetTriangleBoundingBox(void * D, void *K)
{
	Triangle *X = D;	
	double *N = K;	
	N[0] = (X->tminX);
	N[1] = (X->tmaxX);
	N[2] = (X->tminY);
	N[3] = (X->tmaxY);
};
Shape *CreateCircle(double radius, double originX, double originY){
	Circle *X = malloc(sizeof(Circle));
	Shape *L = malloc(sizeof(Shape));	
	L->self = X;
	L->GetBoundingBox = GetCircleBoundingBox;
	L->GetArea = GetCircleArea;	
	X->radius = radius;
	X->centerX = originX;
	X->centerY = originY;
	return L;
};
Shape *CreateRectangle(double minX, double maxX, double minY, double maxY){
	Rectangle *X = malloc(sizeof(Rectangle));
	Shape *L = malloc(sizeof(Shape));
	L->self = X;
	L->GetBoundingBox = GetRectangleBoundingBox;	
	L->GetArea = GetRectangleArea;
	X->rminX = minX;
	X->rmaxX = maxX;
	X->rminY = minY;
	X->rmaxY = maxY; 
	return L;
};
Shape *CreateTriangle(double pt1X, double pt2X, double minY, double maxY){
	Triangle *X = malloc(sizeof(Triangle));
	Shape *L = malloc(sizeof(Shape));	
	L->self = X;	
	X->tminY = minY;
	X->tmaxY = maxY;
	X->tminX = pt1X;
	X->tmaxX = pt2X;
	
	L->GetArea = GetTriangleArea;
	L->GetBoundingBox = GetTriangleBoundingBox;
	return L;
}; 
/* DO NOT MODIFY AFTER THIS POINT */
void
PrintTriangle(Triangle *t)
{
    double bbox[4];
    double area;
    area = GetTriangleArea(t);
    GetTriangleBoundingBox(t, bbox);
    printf("Triangle has area %f and bounding box [%f->%f], [%f->%f]\n",
           area, bbox[0], bbox[1], bbox[2], bbox[3]);
}

void
PrintRectangle(Rectangle *r)
{
    double bbox[4];
    double area;
    area = GetRectangleArea(r);
    GetRectangleBoundingBox(r, bbox);
    printf("Rectangle has area %f and bounding box [%f->%f], [%f->%f]\n",
           area, bbox[0], bbox[1], bbox[2], bbox[3]);
}

void
PrintCircle(Circle *c)
{
    double bbox[4];
    double area;
    area = GetCircleArea(c);
    GetCircleBoundingBox(c, bbox);
    printf("Circle has area %f and bounding box [%f->%f], [%f->%f]\n",
           area, bbox[0], bbox[1], bbox[2], bbox[3]);
}

double GetArea(Shape *s){
	return(s->GetArea(s->self));
};
void GetBoundingBox(Shape *s, double *bbox){
	s->GetBoundingBox(s->self, bbox);
};

/* NEW MAIN */

int main()
{
    Shape *shapes[9];
    int    i;
    shapes[0] = CreateCircle(1, 0, 0);
    shapes[1] = CreateCircle(1.5, 6, 8);
    shapes[2] = CreateCircle(0.5, -3, 4);

    shapes[3] = CreateRectangle(0, 1, 0, 1);
    shapes[4] = CreateRectangle(1, 1.1, 10, 20);
    shapes[5] = CreateRectangle(1.5, 3.5, 10, 12);

    shapes[6] = CreateTriangle(0, 1, 0, 1);
    shapes[7] = CreateTriangle(0, 1, 0, 0.1);
    shapes[8] = CreateTriangle(0, 10, 0, 50);

    for (i = 0 ; i < 9 ; i++)
    {
        double bbox[4];
        printf("Shape %d\n", i);
        printf("\tArea: %f\n", GetArea(shapes[i]));
        GetBoundingBox(shapes[i], bbox);
        printf("\tBbox: %f-%f, %f-%f\n", bbox[0], bbox[1], bbox[2], bbox[3]);
    }
}
