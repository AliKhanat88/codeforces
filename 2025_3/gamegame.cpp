#include <bits/stdc++.h>
using namespace std;
void solve(){
    int n;
    cin >> n;
    vector<int> arr(n);

    
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    int count;
    // cout  << "0" << endl; 
    for(int b = 30; b >= 0; b--){
        count = 0;
        for(int i = 0; i < n; i++){
            if (arr[i] & (1 << b)){
                count += 1;
            }
        }
        if(count % 2 == 1){
            break;
        }
    }
    // cout << count << endl;
    bool can;
    if(count % 2 == 0){
        cout << "DRAW" << endl;
    }else{
        if((count / 2) % 2 == 1){
            can = false;
        }else{
            can = true;
        }

        if(can){
            cout << "WIN" << endl;
        }else{
            if((n - count) % 2 == 1){
                cout << "WIN" << endl;
            }else{
                cout << "LOSE" << endl;
            }
            
        }
    }
}

int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}
