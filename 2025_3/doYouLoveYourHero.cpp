#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;

    vector<pair<int, int>> arr;

    int x = 0;
    int y = 0;
    int cur = 1;
    while (n > 0){
        arr.push_back(make_pair(x, y));
        x += 1;
        cur = 1;
        while(cur <= n){
            arr.push_back(make_pair(x, y));
            n -= cur;
            cur += 1;
            x += 1;
        }
        y += 1;
    }
    cout << arr.size() << endl;
    for(int i = 0; i < arr.size(); i ++){
        cout << arr[i].first << " " << arr[i].second << endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}