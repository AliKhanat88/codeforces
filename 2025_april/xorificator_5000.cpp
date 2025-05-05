#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll xor_t(ll x){
    if (x % 4 == 0){
        return x;
    }else if(x % 4 == 1){
        return 1;
    }else if(x % 4 == 2){
        return x + 1;
    }else{
        return 0;
    }
}
void solve(){
    ll l, r, i, k;
    cin >> l >> r >> i >> k;

    ll new_l = (l - k + (1ll << i) - 1) >> i;
    ll new_r = ( r - k) >> i;
    // cout << new_l << " " << new_r << endl;

    ll other = (xor_t(new_r) ^ xor_t(new_l)) << i;
    // if((l - k - 1) < 0){
    //     new_l -= 1;
    // }
    // if((r - k) < 0){
    //     new_r -= 1;
    // }
    if(((r - k) / (1 << i) - (l - k - 1) / (1 << i)) & 1){
        other = other ^ k;
    }
    cout << ((xor_t(r) ^ xor_t(l-1)) ^ (other)) << endl;
}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}