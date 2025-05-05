#include <bits/stdc++.h>
#define ll long long
#define hello cout << "Hello" << endl
using namespace std;

void solve(){
    int n;
    cin >> n;
    
    map<int, multiset<int>> mapi;
    vector<int> arr(n);
    int temp;
    for(int i = 0; i < n; i ++){
        cin >> arr[i];
        temp = arr[i];
        temp = temp & (~(1 << 0));
        temp = temp & (~(1 << 1));
        mapi[temp].insert(arr[i]);
    }
    map<int, multiset<int>::iterator> iters;
    for(auto &[key, val]: mapi){
        iters[key] = val.begin();
    }

    for(int i = 0; i < n; i ++){
        temp = arr[i];
        temp = temp & (~(1 << 0));
        temp = temp & (~(1 << 1));
        cout << *iters[temp] << " ";
        iters[temp]++;
    }
    cout << endl;

    
    

    

}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}