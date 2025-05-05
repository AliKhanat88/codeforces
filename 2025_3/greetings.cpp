#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <bits/stdc++.h>

using namespace __gnu_pbds;
using namespace std;
template<typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;


void solve(){
    int n;
    cin >> n;
    vector<pair<int, int>> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i].first;
        cin >> arr[i].second;
    }

    

    sort(arr.begin(), arr.end(), [](pair<int, int> a, pair<int, int> b){
        if (a.first > b.first){
            return true;
        }else if (a.first < b.first){
            return false;
        }else{
            return a.second > b.second;
        }
    });
    // cout << "Test" << endl << n << endl;
    // for(int i = 0; i < n; i++){
    //     cout << arr[i].first << " " << arr[i].second << endl;
    // }

    ordered_set<int> new_arr;
    long long sumi = 0;
    for(int i = 0; i < n; i++){
        sumi += new_arr.order_of_key(arr[i].second+1) - new_arr.order_of_key(arr[i].first);
        new_arr.insert(arr[i].second);
    }

    cout << sumi << endl;
}

int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}
