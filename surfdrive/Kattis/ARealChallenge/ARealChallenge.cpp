/*#include<iostream>
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <limits>

using namespace std;

int main()
{
	int val;
	cin >> val;
	cout << std::setprecision(10) << sqrt((double)val)*4;
}*/
#include <iostream>
#include <iomanip>
#include <cmath>
#include <limits>


int main ()
{
  long long int val;
  std::cin >> val;
  std::cout << std::setprecision(50) << sqrt(val)*4.0 << std::endl;
/*  double param, result;
  param = (double) val;
  //param = 1024.0;
  result = sqrt (param)*4;
  printf ("%.7f", result );
  return 0;*/
}