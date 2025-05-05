#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;

    vector <long long> arr(2 * n);

    for(int i = 0; i < 2 * n; i++){
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());

    long long sumi1 = 0;
    long long sumi2 = 0; 
    for(int i = 0; i < n-1; i ++){
        sumi1 += arr[i];
    }
    for(int i= n-1; i < 2 * n - 1; i++){
        sumi2 += arr[i];
    }
    // cout << "Sums " << sumi1 << " " << sumi2 << endl;
    cout << arr[2 * n - 1] << " ";
    arr.insert(arr.begin()+0, sumi2 + arr[2*n-1] - sumi1);
    for(int i = 0; i < n; i++){
        cout << arr[i] << " " << arr[i+n] << " ";
    }
    cout << endl;
}



int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}