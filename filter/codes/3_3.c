#include<stdio.h>
#include<stdlib.h>
int main()
{
    FILE* f = NULL;
    f = fopen("data.dat","w");
    double x[6] ={1.0,2.0,3.0,4.0,2.0,1.0};
    int k=20; 
    double y[20]={0.0};
    y[0] = x[0];
    y[1] = -0.5*y[0]+x[1];


    for(int n=2;n<k-1;n++)
    {
        if (n < 6)
		    y[n] = -0.5*y[n-1]+x[n]+x[n-2];
	    else if (n > 5 && n < 8)
		    y[n] = -0.5*y[n-1]+x[n-2];
	    else
		    y[n] = -0.5*y[n-1];
    }  
    for(int i=0;i<k-1;i++)
    {
        fprintf(f,"%lf ",y[i]);
    } 
}
