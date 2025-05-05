#include <bits/stdc++.h>
#define ll long long
#define hello cout << "Hello" << endl
using namespace std;

void solve(){
    int n;
    cin >> n;
    int k;
    cin >> k;

    vector<int> arr(n);
    for(int i = 0; i < n; i ++){
        cin >> arr[i];
    }

    ll ans = 0;
    vector<int> new_arr(n);
    for(int i = 0; i < n; i++){
        ans += (arr[i] / k);
        new_arr[i] = arr[i] % k;
    }

    sort(new_arr.begin(), new_arr.end());

    int l = 0;
    int r = n-1;
    while(l < r){
        if (new_arr[l] + new_arr[r] >= k){
            ans += 1;
            l += 1;
            r -= 1;
        }else{
            l += 1;
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