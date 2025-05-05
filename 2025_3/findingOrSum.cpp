#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll query(ll x){
    cout << x << endl;
    cout.flush();
    ll temp;
    cin >> temp;
    return temp;
}

void solve(){
    ll n1 = 0;
    ll n2 = 0;
    for(int i = 0; i < 30; i++){
        if(i%2 == 1){
            n2 += (1ll << i);
        }else{
            n1 += (1ll << i);
        }
    }
    ll r1;
    ll r2;
    r1 = query(n1);
    r2 = query(n2);
    cout << "!" << endl;
    cout.flush();

    ll m;
    cin >> m;
    
    vector<int> arr(31);
    for(int i = 1; i < 30; i+=2){
        if(r1 & (1 << i)){ // 1
            if(r1 & (1 << (i+1))){ // 1
                arr[i] = 2;
            }else{ // 0
                arr[i] = 0;
            }
        }else{
            arr[i] = 1;
        }
    }

    if(r2 & (1 << 0)){ // 1
        arr[0] = 1;
    }else{
        if(r2 & (1 << 1)){ // 1
            arr[0] = 2;
        }else{ // 0
            arr[0] = 0;
        }
    }
    

    for(int i = 2; i < 30; i+=2){
        if(r2 & (1 << i)){ // 1
            if(r2 & (1 << (i+1))){ // 1
                arr[i] = 2;
            }else{ // 0
                arr[i] = 0;
            }
        }else{
            arr[i] = 1;
        }
    }
    ll ans = 0;
    ll c = 0;
    for(int i = 0; i <= 30; i++){
        if(m & (1ll << i)){ // 1
            if(c == 1){
                ans += (1ll << i);
            }
            c = 1;
        }else{
            if(c + arr[i] == 1){
                ans += (1ll << i);
                c = 0;
            }else if(c + arr[i] == 2){
                c = 1;
            }else if(c + arr[i] == 3){
                c = 1;
                ans += (1ll << i);
            }else{
                c = 0;
            }
        }
    }
    cout << ans << endl;

    
}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}