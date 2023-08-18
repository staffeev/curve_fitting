#include <math.h> 

/*--------------------------------------------------------------*/
double evalfpoly(int order, double x, double *c)
/*--------------------------------------------------------------*/
{
  int i,j;
  double y=c[0];
  x=(x-(0.09746145000000001))/(0.1408816797092595);
  for(i=1,j=1;j<=order;j+=2,i++)
    y += c[j]*cos(i*x)+c[j+1]*sin(i*x);
  return y;
}
 
/*--------------------------------------------------------------*/
double fourier(double x)
/*--------------------------------------------------------------*
   TableCurve Function: C:\\Users\\Thunderobot\\Desktop\\curve_fitting\\fourier.c Aug 18, 2023 11:40:29 AM 
   Test 
   X= Y 
   Y= X 
   Eqn# 6850  Fourier Series Polynomial 10x2 
   r2=0.4926363883363351 
   r2adj=0.4830720832690667 
   StdErr=0.1076454308942949 
   Fstat=54.13174697273537 
   a= 77576.40575203449 
   b= -13947.55144544388 
   c= -144763.092341742 
   d= -117396.557425391 
   e= 22889.73968917343 
   f= 24561.81611236296 
   g= 82308.13325823155 
   h= 49415.54404997974 
   i= -20247.77107238413 
   j= -13337.99691004509 
   k= -25019.94821279292 
   l= -10434.0867759103 
   m= 7036.740700009835 
   n= 2910.598277850978 
   o= 3453.157192379598 
   p= 852.0985896508907 
   q= -898.3316247063267 
   r= -186.3878645903396 
   s= -139.2875217135762 
   t= -11.24420340265074 
   u= 19.7710226697559 
 *--------------------------------------------------------------*/
{
  double y;
  static double c[]= { 
    77576.40575203449, 
    -13947.55144544388, 
    -144763.0923417420, 
    -117396.5574253910, 
    22889.73968917343, 
    24561.81611236296, 
    82308.13325823155, 
    49415.54404997974, 
    -20247.77107238413, 
    -13337.99691004509, 
    -25019.94821279292, 
    -10434.08677591030, 
    7036.740700009835, 
    2910.598277850978, 
    3453.157192379598, 
    852.0985896508907, 
    -898.3316247063267, 
    -186.3878645903396, 
    -139.2875217135762, 
    -11.24420340265074, 
    19.77102266975590, 
    }; 
  y=evalfpoly(20,x,c); 
  return(y);
}
 
