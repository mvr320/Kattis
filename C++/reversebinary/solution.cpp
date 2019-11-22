#include<iostream>
using namespace std;
int main()
{
    int result = 0;
    int val;
    int temp;
    cin >> val;
    while(!(val==0)){
        result = result << 1;
        result += val &1;
        val = val >> 1;
    }
    cout << result;
}