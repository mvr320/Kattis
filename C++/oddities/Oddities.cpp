#include<iostream>

using namespace std;

int main()
{
	int val;
    int cases;
    cin >> cases;
    for(int i=0; i<cases; i++){
    	cin >> val;
    	if(val%2==0){
    		cout << val << " is even" << endl;
    	} else {
    		cout << val << " is odd" << endl;
    	}
    }
}