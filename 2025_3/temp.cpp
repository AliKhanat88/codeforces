
#include <bits/stdc++.h>

using namespace std;

int main(){
    map<int, int> seti;

    vector<int> arr = {1, 2, 3,5,6,3,3,3,6,4,5};
    
    for(int num: arr){
        seti[num] += 1;
    }
    // cout << list.end() << endl;
    // for(int)
    auto it = seti.upper_bound(6);
    if (it != seti.end()){
        cout << (*it).first << endl;
    }
    cout << seti.end()->first << endl;
}