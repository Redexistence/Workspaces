#include <iostream>
#include <vector>

using namespace std;

const int MAX_VAL = 2000000;
int freq[2 * MAX_VAL + 5];

long long dp[5005][5005];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("threesum.in", "r", stdin);
    freopen("threesum.out", "w", stdout);
    #endif

    int n,q;
    if (!(cin >> n >> q)) return 0;

    vector<int> a(n+1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    for (int i = 1; i <= n; ++i) {
        for (int k = i + 1; k <= n; ++k){
            long long target = -a[i] - a[k];
            if (target >= -MAX_VAL && target <= MAX_VAL) {
                dp[i][k] = freq[target + MAX_VAL];
            }
            freq[a[k] + MAX_VAL]++;
        }
        for (int k = i + 1; k <= n; ++k) {
            freq[a[k] + MAX_VAL]--;
        }
    }

    for (int len = 3; len <= n; ++len) {
        for (int i = 1; i <= n - len + 1; ++i) {
            int k = i + len - 1;
            dp[i][k] += dp[i + 1][k] + dp[i][k - 1] - dp[i + 1][k - 1];
        }
    }

    for (int i = 0; i < q; ++i) {
        int u, v;
        cin >> u >> v;
        cout << dp[u][v] << "\n";
    }

    return 0;
}