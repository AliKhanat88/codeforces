#include <bits/stdc++.h>

using namespace std;

void solve(){
    int n;
    cin >> n;
    map<int, vector<int>> mapi;

    vector<int> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
        mapi[arr[i]].emplace_back(i);
    }
    vector<int> ans;
    int missing;
    int to_replace;
    while (true){
        missing = -1;
        to_replace = -1;
        for(int i = 0; i <= n; i++){
            if (to_replace == -1 && (mapi[i].size() > 1 || (mapi[i].size() == 1 && i == n))){
                to_replace = i;
            }
            if (missing == -1 && (mapi[i].size() == 0)){
                missing = i;
            }
        }
        if(to_replace == -1){
            break;
        }
        ans.push_back(mapi[to_replace].back());
        mapi[to_replace].pop_back();
        mapi[missing].push_back(ans.back());
        arr[ans.back()] = missing;
    }
    for(int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    cout << endl;

    set<int> done;
    int cur = arr[n-1];
    arr[n-1] = n;
    done.insert(n-1);
    ans.push_back(n-1);
    int temp;
    for(int i=0; i < n; i++){
        if (done.find(cur) == done.end()){
            done.insert(cur);
            temp = arr[cur];
            arr[cur] = cur;
            ans.push_back(cur);
            cur = temp;
            

        }else if(cur-1 >= 0 && done.find(cur-1) == done.end()){
            done.insert(cur-1);
            temp = arr[cur-1];
            arr[cur-1] = cur;
            ans.push_back(cur-1);
            cur = temp;
        }else{
            break;
        }

    }
    cout << ans.size() << endl;
    for (int i = 0; i < ans.size(); i++){
        cout << ans[i]+1 << " ";
    }
    cout << endl;
    

}
int main(){
    int t;
    cin >> t;
    while (t--){
        solve();
    }
}