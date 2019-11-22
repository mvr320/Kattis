#include<iostream>

using namespace std;

int main()
{
    int bsum = 0;
    int bplay = 0;
    for(int i=1; i<6; i++){
    	int sum = 0;
    	for(int j=0; j<4; j++){
    		int val = 0;
    		cin >> val;
    		sum += val;
    	}
    	if(sum>bsum){
    		bsum=sum;
    		bplay=i;
    	}
    }
    cout << bplay << " " << bsum << endl;
}