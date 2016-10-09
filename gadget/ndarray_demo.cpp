#include <cstdarg>
#include <iostream>
#include "ndarray.h"
using namespace std;
void plusxy(ndarray<int> &a){
    if(a.dim!=2)
        return;
    for(int i=0;i<a.shape[0];i++){
        for(int j=0;j<a.shape[1];j++){
            a(i,j)=i+j;
        }
    }
}
int main(){
    ndarray<int> a={3,4};
    int i;
    plusxy(a);
    cout<<i<<endl;
    for(int i=0;i<3;i++){
        for(int j=0;j<4;j++){
            cout<<a(i,j)<<' ';
        }
        cout<<'\n';
    }
}
