#include <bits/stdc++.h>
using namespace std;

#define ll long long

void solve(){
    ll x, y, px_py, py, mx, mx_my, my, px;
    cin >> x >> y >> px_py >> py >> mx >> mx_my >> my >> px;

    auto cost = [&](ll temp){
        ll temp_cost = 0;
        if(temp >= 0){
            temp_cost += (px_py * temp); 
        }else{
            temp_cost += (mx_my * abs(temp)); 
        }
        ll tempx = x - temp;
        ll tempy = y - temp;
        if (tempx >= 0){
            temp_cost += (px * tempx);
        }else{
            temp_cost += (mx * abs(tempx));
        }
        if (tempy >= 0){
            temp_cost += (py * tempy);
        }else{
            temp_cost += (my * abs(tempy));
        }
        return temp_cost;
    };


    ll l = 0, r = 1LL << 30;
    ll m1 = 0;
    ll m2 = 0;
    while(l + 1 < r){
        // cout << l << r << endl;
        m1 = l + (r - l) / 3;
        m2 = r - (r - l) / 3;
        if (cost(m1) >= cost(m2)){
            l = m1 + 1;
        }else{
            r = m2 - 1;
        }
    }
    ll mini = min(cost(l), cost(r));
    
    l = -(1LL << 30), r = 0;
    while(l + 1 < r){
        m1 = l + (r - l) / 3;
        m2 = r - (r - l) / 3;
        if (cost(m1) >= cost(m2)){
            l = m1 + 1;
        }else{
            r = m2 - 1;
        }
    }
    mini = min(mini, min(cost(l), cost(r)));

    cout << mini << endl;

}

int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}