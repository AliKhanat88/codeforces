#include <iostream>
#include <vector>
#include <unordered_map>
#include <numeric> // Include for accumulate
#include <cmath>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    cin >> n;
    
    vector<long> arr(n);
    unordered_map<long long, int> myDict;
    long long sumi = 0;

    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        myDict[arr[i]]++;
        sumi = sumi + arr[i];
    }
    
    vector<long long> myQueue = {sumi};

    while (!myQueue.empty()) {
        long long cur = myQueue.front();
        myQueue.erase(myQueue.begin());

        if (myDict[cur] > 0) {
            myDict[cur]--;
        } else if ((cur == 1 && myDict[cur] <= 0) || myQueue.size() > n + 5) {
            cout << "NO" << endl;
            return;
        } else {
            myQueue.push_back(ceil(static_cast<double>(cur) / 2));
            myQueue.push_back(floor(static_cast<double>(cur) / 2));
        }
    }

    if (all_of(myDict.begin(), myDict.end(), [](const pair<int, int>& elem) { return elem.second == 0; })) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        solve();
    }

    return 0;
}
