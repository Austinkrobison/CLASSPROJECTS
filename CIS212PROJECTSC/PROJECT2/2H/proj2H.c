#include <stdio.h>
/* Place your struct definitions for Circle, Triangle, and Rectangle here */

typedef struct{
	double rminX, rminY, rmaxX, rmaxY;
} Rectangle;
typedef struct{
	double tminY, tminX, tmaxX, tmaxY;
}Triangle;

typedef struct{
	double radius, centerX, centerY;
} Circle;

/* Define these 9 functions */
void InitializeCircle(Circle *X, double radius, double originX, double originY)
{
	X->radius = radius;
	X->centerX = originX;	
	X->centerY = originY;

};

void InitializeRectangle(Rectangle *X, double minX, double maxX, double minY, double maxY)
{
	X->rminX = minX;
	X->rmaxX = maxX;
	X->rminY = minY;
	X->rmaxY = maxY;
};

void InitializeTriangle(Triangle *X, double pt1X, double pt2X, double minY, double maxY)
{
	X->tminY = minY;
	X->tmaxY = maxY;
	X->tminX = pt1X;
	X->tmaxX = pt2X;

};


double GetCircleArea(Circle *X)
{
	return(X->radius * X-> radius *3.14159);
};

double GetRectangleArea(Rectangle *X)
{
	return(  ((X->rmaxX) - (X->rminX)) * ((X->rmaxY) - (X->rminY))  ); 
};

double GetTriangleArea(Triangle *X)
{
	return( (((X->tmaxY) - (X->tminY)) /2) *((X->tmaxX) - (X->tminX)) );  
};


void GetCircleBoundingBox(Circle *X, double *N)
{
	N[0] = (X->centerX)-(X->radius);
	N[1] = (X->centerX)+(X->radius);
	N[2] = (X->centerY)-(X->radius);
	N[3] = (X->centerY)+(X->radius);
};

void GetRectangleBoundingBox(Rectangle *X, double *N)
{
	N[0] = (X->rminX);
	N[1] = (X->rmaxX);
	N[2] = (X->rminY);
	N[3] = (X->rmaxY);
};

void GetTriangleBoundingBox(Triangle *X, double *N)
{
	N[0] = (X->tminX);
	N[1] = (X->tmaxX);
	N[2] = (X->tminY);
	N[3] = (X->tmaxY);

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

int main()
{
    Circle c;
    Triangle t;
    Rectangle r;

    InitializeCircle(&c, 1, 0, 0);
    PrintCircle(&c);
    InitializeCircle(&c, 1.5, 6, 8);
    PrintCircle(&c);
    InitializeCircle(&c, 0.5, -3, 4);
    PrintCircle(&c);

    InitializeRectangle(&r, 0, 1, 0, 1);
    PrintRectangle(&r);
    InitializeRectangle(&r, 1, 1.1, 10, 20);
    PrintRectangle(&r);
    InitializeRectangle(&r, 1.5, 3.5, 10, 12);
    PrintRectangle(&r);

    InitializeTriangle(&t, 0, 1, 0, 1);
    PrintTriangle(&t);
    InitializeTriangle(&t, 0, 1, 0, 0.1);
    PrintTriangle(&t);
    InitializeTriangle(&t, 0, 10, 0, 50);
    PrintTriangle(&t);
}
