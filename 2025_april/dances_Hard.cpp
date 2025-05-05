#include <bits/stdc++.h>
using namespace std;
#define ll long long

void solve(){
    int n;
    cin >> n;

    multiset<int> arr = {1};
    int x;
    for(int i = 0; i < n-1; i ++){
        cin >> x;
        arr.insert(x);
    }
    multiset<int> brr;
    for(int i = 0; i < n; i ++){
        cin >> x;
        brr.insert(x);
    }
    auto start_a = arr.begin();
    auto start_b = brr.begin();
    ll count = 0;
    for(int i = 0; i < n; i++){
        if(*start_a >= *start_b){
            arr.erase(arr.end());
            brr.erase(brr.begin());
            count += 1;
        }else{
            start_a++;
            start_b++;
        }
    }
    cout << count << endl;
}
int main(){
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}