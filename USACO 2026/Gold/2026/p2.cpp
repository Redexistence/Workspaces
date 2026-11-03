#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct FenwickTree {
    int n;
    vector<int> tree;
    FenwickTree(int n) : n(n), tree(n + 1, 0) {}

    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    vector<int> vals(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        vals[i] = a[i];
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    auto get_compressed = [&](int x) {
        return lower_bound(vals.begin(), vals.end(), x) - vals.begin() + 1;
    };

    FenwickTree ft_left(vals.size());
    vector<int> smaller_left(n, 0);
    for (int i = 0; i < n; ++i) {
        int idx = get_compressed(a[i]);
        smaller_left[i] = ft_left.query(idx - 1);
        ft_left.add(idx, 1);
    }

    FenwickTree ft_right(vals.size());
    vector<int> smaller_right(n, 0);
    for (int i = n - 1; i >= 0; --i) {
        int idx = get_compressed(a[i]);
        smaller_right[i] = ft_right.query(idx - 1);
        ft_right.add(idx, 1);
    }

    long long total_coins = 0;
    for (int i = 0; i < n; ++i) {
        total_coins += min(smaller_left[i], smaller_right[i]);
    }

    cout << total_coins << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}