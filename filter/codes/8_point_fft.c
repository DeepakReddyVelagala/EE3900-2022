#include<stdio.h>
#include<stdlib.h>
#include<complex.h>

int main()
{
    double x[8] = {0,1,2,3,4,2,1,0};

    // double Xe[4] = {0,2,4,1};
    // double Xo[4] = {1,3,2,0};
    // X1 = F4.Xe + D4.F4.Xo
    // X2 = F4.Xe - D4.F4.Xo
    // DF4 = D4*F4
    // where,
    // double complex F4[4][4] = {{-I,-1,I,1},{-1,1,-1,1},{I,-1,-I,1},{1, 1,1, 1}};
    // double complex DF4[4][4] = {{-I,-1,I,1},{I,-I,I,-I},{-I,1,I,-1},{I,I,I, I}};
    // a[4] = F4*xe and b[4] = D4*F4*xo

    double complex a[4],b[4];

    a[0] = x[6]-x[2] + I*(x[4]-x[0]);
    a[1] = x[6]+x[2] - (x[4]+x[0]);
    a[2] = x[6]-x[2] - I*(x[4]-x[0]);
    a[3] = x[6]+x[2] + (x[4]+x[0]);

    b[0] = (x[7]-x[3]) + I*(x[5]-x[1]);
    b[1] = -I*(x[7]-x[3]) + I*(x[5]+x[1]);
    b[2] = -(x[7]-x[3]) + I*(x[5]-x[1]);
    b[3] = I*(x[7]+x[3]) + I*(x[5]+x[1]);

    double complex X1[4], X2[4];

    for(int i=0;i<4;i++)
    {
        X1[i] = a[i] + b[i];
        X2[i] = a[i] - b[i];
    }

    for(int i=0;i<4;i++)
    {
        printf("%.1lf + I*(%.1lf)\n",creal(X1[i]), cimag(X1[i]));
    }
    for(int i=0;i<4;i++)
    {
        printf("%.1lf + I*(%.1lf)\n",creal(X2[i]), cimag(X2[i]));
    }
    return 0;
}