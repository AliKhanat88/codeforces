#include <bits/stdc++.h>
using namespace std;

const long long INF = 2 ^ 60;

class MinSegTree {
public:
    int n;
    vector<long long> tree;

    MinSegTree(vector<long long>& arr) {
        n = arr.size();
        tree.resize(n * 2);
        for (int i = 0; i < n; ++i) {
            tree[i + n] = arr[i];
        }
        for (int i = n - 1; i > 0; --i) {
            tree[i] = min(tree[i * 2], tree[i * 2 + 1]);
        }
    }

    void update(int index, long long val) {
        int i = index + n;
        tree[i] = val;
        while (i > 1) {
            i /= 2;
            tree[i] = min(tree[i * 2], tree[i * 2 + 1]);
        }
    }

    long long query(int l, int r) {
        l += n;
        r += n;
        long long ans = INF;
        while (l < r) {
            if (l % 2 == 1) {
                ans = min(ans, tree[l]);
                ++l;
            }
            if (r % 2 == 1) {
                --r;
                ans = min(ans, tree[r]);
            }
            l /= 2;
            r /= 2;
        }
        return ans;
    }
};

class MaxSegTree {
public:
    int n;
    vector<long long> tree;

    MaxSegTree(vector<long long>& arr) {
        n = arr.size();
        tree.resize(n * 2);
        for (int i = 0; i < n; ++i) {
            tree[i + n] = arr[i];
        }
        for (int i = n - 1; i > 0; --i) {
            tree[i] = max(tree[i * 2], tree[i * 2 + 1]);
        }
    }

    void update(int index, long long val) {
        int i = index + n;
        tree[i] = val;
        while (i > 1) {
            i /= 2;
            tree[i] = max(tree[i * 2], tree[i * 2 + 1]);
        }
    }

    long long query(int l, int r) {
        l += n;
        r += n;
        long long ans = -INF;
        while (l < r) {
            if (l % 2 == 1) {
                ans = max(ans, tree[l]);
                ++l;
            }
            if (r % 2 == 1) {
                --r;
                ans = max(ans, tree[r]);
            }
            l /= 2;
            r /= 2;
        }
        return ans;
    }
};

void solve() {
    int n, q;
    cin >> n >> q;
    vector<long long> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    vector<long long> left(n), right(n);
    for (int i = 0; i < n; ++i) {
        left[i] = i + arr[i];
        right[i] = (n - i - 1) + arr[i];
    }

    MinSegTree leftMin(left), rightMin(right);
    MaxSegTree leftMax(left), rightMax(right);

    auto find_max = [&](int index) {
        long long org_val1 = left[index];
        long long org_val2 = right[index];
        long long maxi = max({
            org_val1 - leftMin.query(index, n),
            leftMax.query(0, index + 1) - org_val1,
            org_val2 - rightMin.query(0, index + 1),
            rightMax.query(index, n) - org_val2
        });
        return maxi;
    };

    priority_queue<pair<long long, int>> heap;
    for (int i = 0; i < n; ++i) {
        heap.push({-find_max(i), i});
    }
    cout << -heap.top().first << "\n";

    for (int i = 0; i < q; ++i) {
        int pi;
        long long num;
        cin >> pi >> num;
        --pi;
        arr[pi] = num;
        leftMin.update(pi, num + pi);
        rightMin.update(pi, num + n - pi - 1);
        leftMax.update(pi, num + pi);
        rightMax.update(pi, num + n - pi - 1);
        left[pi] = num + pi;
        right[pi] = num + n - pi - 1;

        heap.push({-find_max(pi), pi});
        while (!heap.empty()) {
            if (find_max(heap.top().second) != -heap.top().first) {
                auto temp = heap.top();
                heap.pop();
                heap.push({-find_max(temp.second), temp.second});
            } else {
                break;
            }
        }
        cout << -heap.top().first << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
