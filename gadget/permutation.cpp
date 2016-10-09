#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
void permu(vector<int> &a, uint start = 0);

inline bool check_do(vector<int> &a, uint pos) {
    for(uint i = 0; i < pos; i++) {///< comment loop to give all permutations
        if(uint(abs(a[pos] - a[i])) == pos - i)
            return false;
    }
    permu(a, pos + 1);
    return true;
}

void permu(vector<int> &a, uint start) {
    int orig = a[start];
    static uint num = 0;
    if(start == a.size()) {
        cout << ++num << ":\t";
        for(uint i = 0; i < a.size(); i++)
            cout << a[i] << "\t";
        cout << endl;
        return;
    }
    check_do(a, start);
    for(uint i = start + 1; i < a.size(); i++) {
        a[start] = a[i];
        a[i] = orig;
        check_do(a, start);
        a[i] = a[start];
    }
    a[start] = orig;
}

inline void permunum(int serial, int n){
    for(int i=n; i>0; i--){
        cout<<serial%i<<'\t';
        serial/=i;
    }
    cout<<'\n';
}
void permuint(uint n){
    vector<int> a;
    for(uint i = 0; i < n; i++)
        a.push_back(i + 1);
    for(uint i = 0; i < a.size(); i++)
        cout<<a[i];
    cout<<'\n';
    permu(a);
}
void fillone(vector<int> &a, int slot, int coin){
    static int cnt=0;
    if(!coin){
        cout<<++cnt<<":\t";
        for(int i=0;i<a.size();i++){
            cout<<a[i]<<'\t';
        }
        cout<<'\n';
        return;
    }
    int start=a.size()-slot, end=a.size()-coin+1;
    if(slot==coin){
        cout<<++cnt<<":\t";
        for(int i=0;i<start;i++){
            cout<<a[i]<<'\t';
        }
        for(int i=0;i<slot;i++){
            cout<<"1\t";
        }
        cout<<'\n';
        return;
    }
    for(int i=start;i<end;i++){
        a[i]=1;
        fillone(a, a.size()-i-1, coin-1);
        a[i]=0;
    }
}
void combination(int slot, int coin){
    vector<int> a(slot, 0);
    fillone(a, slot, coin);
}

int main() {
    combination(10, 5);
}
