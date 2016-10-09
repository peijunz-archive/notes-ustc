#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
void permu(vector<int> &a, uint start=0);

bool check_do(vector<int> &a, uint pos){
    for(uint i=0;i<pos;i++){
        if(uint(abs(a[pos]-a[i]))==pos-i)
            return false;
    }
    permu(a, pos+1);
    return true;
}

void permu(vector<int> &a, uint start){
    int orig=a[start];
    if(start == a.size()){
        for(uint i=0;i<a.size();i++)
            cout<<a[i]<<"\t";
        cout<<endl;
        return;
    }
    check_do(a, start);
    for(uint i=start+1;i<a.size();i++){
        a[start]=a[i];
        a[i]=orig;
        check_do(a, start);
        a[i]=a[start];
    }
    a[start]=orig;
}
int main()
{
    vector<int> a;
    for(uint i=0;i<5;i++)
        a.push_back(i+1);
    permu(a);
}
