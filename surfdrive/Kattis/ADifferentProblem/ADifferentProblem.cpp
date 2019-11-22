#include <iostream>

using namespace std;
int main ()
{
	while(!cin.eof()){
		long long int val1, val2, result;
		cin >> val1 >> val2;
		result = val1 - val2;
		if(result<0){
			result *= -1;
		}
		cout << result << endl;
	}
}