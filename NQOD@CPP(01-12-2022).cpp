#include <bits/stdc++.h> // header file includes every Standard library
using namespace std;
int main() {
	long long int a,b,c,d,e,count=0;
    cin>>a>>b>>c;
    while(a>0)
    {
        cin>>d>>e;
        if(d<b&&e>c)
        {
            count++;
        }
        a--;
    }
    if(count>0){cout<<"Yes";}
    else{cout<<"No";}
}
