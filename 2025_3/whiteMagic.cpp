#include <bits/stdc++.h>
#define ll long long
#define hello cout << "Hello" << endl
using namespace std;

void solve(){
    int n;
    cin >> n;

    vector<int> arr;
    int temp;
    bool isfirst = true;
    for(int i = 0; i < n; i++){
        cin >> temp;
        if(isfirst && temp == 0){
            arr.push_back(temp);
            isfirst = !isfirst;
        }else if(temp){
            arr.push_back(temp);
        }
    }
    // hello;
    n = arr.size();
    vector<int> suffix(n);
    map<int, int> mapi;
    int cur = 0;
    for(int i = n-1; i >= 0; i--){
        mapi[arr[i]] += 1;
        while(mapi[cur] > 0){
            cur += 1;
        }
        suffix[i] = cur;
    }
    ll mini = 1ll << 50;
    for(int i = 0; i < n - 1; i++){
        mini = min(mini, (ll)arr[i]);
        if (mini < (ll)suffix[i+1]){
            cout << n-1 << endl;
            return;
        }
    }
    cout << n << endl;

}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}