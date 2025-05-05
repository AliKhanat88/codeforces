#include <bits/stdc++.h>

using namespace std;

void solve(){
    int n;
    cin >> n;
    vector<vector<int>> arr(n, vector<int>(3));

    for(int i = 0; i < n; i ++){
        cin >> arr[i][0] >> arr[i][1];
        arr[i][2] = i;
        // cout << arr[i][0] << " " << arr[i][1] << endl;
    }

    vector<int> ans(n, 0);

    sort(arr.begin(), arr.end());

    multiset<int> seti = {};
    
    // for(auto it = arr.begin(); it != arr.end(); it++){
    //     cout << (*it)[0] << " " << (*it)[1] << endl;
    // }
    auto temp = seti.end();
    int j = 0;
    for(int i = 0; i < n; i ++){
        while(j < n && arr[i][0] == arr[j][0]){
            seti.insert(arr[j][1]);
            j++;
        }
        seti.erase(seti.lower_bound(arr[i][1]));
        temp = seti.lower_bound(arr[i][1]);
        
        if (temp == seti.end()){
            seti.insert(arr[i][1]);
            continue;
        }
        // cout << *temp << " " << arr[i][0] << " " << arr[i][1] << endl;
        ans[arr[i][2]] += ((*temp) - arr[i][1]);
        seti.insert(arr[i][1]);
    }

    sort(arr.begin(), arr.end(), [](vector<int> a, vector<int> b){
     return (a[1] > b[1]);   
    });
    
    seti = {};
    
    // for(auto it = arr.begin(); it != arr.end(); it++){
    //     cout << (*it)[0] << " " << (*it)[1] << endl;
    // }
    temp = seti.end();
    // cout << n << endl;
    j = 0;
    for(int i = 0; i < n; i ++){
        while(j < n && arr[i][1] == arr[j][1]){
            seti.insert(arr[j][0]);
            j++;
        }
        seti.erase(seti.lower_bound(arr[i][0]));
        temp = seti.upper_bound(arr[i][0]);
        
        if (temp == seti.begin()){
            seti.insert(arr[i][0]);
            continue;
        }
        // cout << *temp << endl;
        temp--;
        ans[arr[i][2]] += (arr[i][0] - (*temp));
        seti.insert(arr[i][0]);
    }

    for (int i = 0; i < n; i++){
        cout << ans[i] << endl;
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--){
        solve();
    }
}
