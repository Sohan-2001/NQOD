#include <bits/stdc++.h> // header file includes every Standard library
using namespace std;

int main() {
	long long int a,b;
    cin>>a>>b;
    long long int arr[a],sum1=0,sum2=0;
    for(long long int i=0; i<a; i++)
    {
        cin>>arr[i];
        sum1=sum1+arr[i];
    }
    sort(arr,arr+a);
    for(long long int i=a-1; i>=0; i--)
    {
        if(b>0)
        {
            sum2=sum2+arr[i];
        }
        else{break;}
        b--;
    }
    if(sum1-sum2>=0)
    {
        cout<<sum1-sum2;
    }
    else{cout<<0;}
    

}
