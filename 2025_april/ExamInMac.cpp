#include <bits/stdc++.h>
#define ll long long
using namespace std;

void solve(){
    ll n,c;
    cin >> n >> c;
    vector<int> arr(n);
    // cout << "Hello World";
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    // cout << "Hello";
    ll ans = 0;
    int even = 0;
    int odd = 0;
    for(int i = n-1; i >= 0; i--){
        ans = ans - (arr[i] / 2 + 1);
        ans = ans - (c - arr[i]);
        if (arr[i] % 2){
            ans = ans + (even);
            even += 1;
            
        }else{
            ans = ans + (odd);
            odd += 1;
            
        }

    }

    cout << ans + ((c + 2) * (c + 1)) / 2 << endl;
    
}



int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}