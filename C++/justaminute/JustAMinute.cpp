#include <iostream>
#include <iomanip>

using namespace std;
int main ()
{
  int count;
  cin >> count;
  int ssumm = 0;
  int rsums = 0;
  for(int i=0; i<count; i++){
  	int smin;
  	int rsec;
  	cin >> smin >> rsec;
  	ssumm += smin;
  	rsums += rsec;
  }
  double result = (double)rsums/((double)ssumm*60.0);
  if(result>1.0){
  	cout << setprecision(20) << result << endl;
  } else {
  	cout << "measurement error";
  }
}