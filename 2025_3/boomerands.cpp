#include <bits/stdc++.h>

using namespace std;

void solve(){
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i]; 
    }

    vector<tuple<int, int>> points;
    vector<tuple<int, int>> two_points;
    vector<tuple<int, int>> three_points;
    vector<tuple<int, int>> ans;
    int q_index = 0;
    int two_q_index = 0;
    int three_q_index = 0;
    int temp_val = n; 
    for(int i = n-1; i >= 0; i--){
        if (arr[i] == 1){
            points.emplace_back(temp_val, i+1);
            ans.emplace_back(temp_val, i+1);
            temp_val -= 1;
        }else if(arr[i] == 2){
            if(q_index >= points.size()){
                cout << -1 << endl;
                return;
            }else{
                // cout << "here in 2 " << get<0>(points[q_index]) << " " << get<1>(points[q_index]) << " " << q_index << endl;
                ans.emplace_back(get<0>(points[q_index]), i+1);
                two_points.emplace_back(get<0>(points[q_index]), i+1);
                q_index += 1;
            }
        }else if(arr[i] == 3){
            if(three_q_index < three_points.size()){
                three_points.emplace_back(temp_val, i+1);
                ans.emplace_back(temp_val, i+1);
                ans.emplace_back(temp_val, get<1>(three_points[three_q_index]));
                three_q_index += 1;

            }else if(two_q_index < two_points.size()){
                three_points.emplace_back(temp_val, i+1);
                ans.emplace_back(temp_val, i+1);
                ans.emplace_back(temp_val, get<1>(two_points[two_q_index]));
                two_q_index += 1;
            }else if(q_index < points.size()){
                three_points.emplace_back(temp_val, i+1);
                ans.emplace_back(temp_val, i+1);
                ans.emplace_back(temp_val, get<1>(points[q_index]));
                q_index += 1;
            }else{
                cout << -1 << endl;
                return;
            }
            temp_val -= 1;
        }
    }
    cout << ans.size() << endl;
    for(auto tup: ans){
        cout << get<0>(tup) << " " << get<1>(tup) << endl;
    }
}

int main(){
    solve();
}