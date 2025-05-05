#include <bits/stdc++.h>
#define ll long long
#define hello cout << "Hello" << endl
using namespace std;

bool check(vector<int> &arr, int k){
    map<int, int> bits;
    for(int i = 0; i < k; i++){
        for(int b = 0; b < 20; b++){
            if(arr[i] & (1 << b)){
                bits[b] += 1;
            }
        }
    }
    ll initial = 0;
    ll temp;
    for(int b = 0; b < 20; b++){
        if(bits[b] > 0){
            initial += (1 << b);
        }
    }
    for(int i = k; i < arr.size(); i++){
        for(int b = 0; b < 20; b++){
            if(arr[i] & (1 << b)){
                bits[b] += 1;
            }
            if(arr[i-k] & (1 << b)){
                bits[b] -= 1;
            }
        }
        temp = 0;
        for(int b = 0; b < 20; b++){
            if(bits[b] > 0){
                temp += (1 << b);
            }
        }
        if(temp != initial){
            return false;
        }
    }
    return true;
}
void solve(){
    int n;
    cin >> n;

    vector<int> arr(n);
    for(int i = 0; i < n; i ++){
        cin >> arr[i];
    }

    int l = 1;
    int r = n;
    int m;
    while (l + 1 < r){
        m = (l + r) / 2;
        if (check(arr, m)){
            r = m;
        }else{
            l = m + 1;
        }
    }

    if (check(arr, l)){
        cout << l << endl;
        return;
    }
    cout << r << endl;
    return;
    

}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}