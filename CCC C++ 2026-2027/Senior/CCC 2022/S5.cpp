#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const long long INF = 1e15;

int N;
vector<vector<long long>> dp;
vector<vector<int>> adj;
vector<long long> C;
string P;

void dfs(int u, int p) {
    bool is_leaf = true;
    for (int v : adj[u]) {
        if (v != p) {
            is_leaf = false;
            dfs(v, u);
        }
    }

    long long pay_cost = C[u];
    long long no_pay_cost = 0;

    for (int v : adj[u]) {
        if (v == p) continue;
        pay_cost += dp[v][0];
        no_pay_cost += dp[v][1];
    }

    if (P[u] == 'Y') {
        dp[u][0] = min(pay_cost, no_pay_cost);
    } else {
        dp[u][0] = min(pay_cost, no_pay_cost);
    }

    if (P[u] == 'Y') {
        dp[u][2] = pay_cost;
    } else {
        if (is_leaf) {
            dp[u][2] = INF;
        } else {
            long long best_child_influence = INF;
            long long sum_dp_v0 = 0;
            for (int v : adj[u]) {
                if (v == p) continue;
                sum_dp_v0 += dp[v][0];
            }
            for (int v : adj[u]) {
                if (v == p) continue;
                if (dp[v][2] != INF) {
                    best_child_influence = min(best_child_influence, sum_dp_v0 - dp[v][0] + dp[v][2]);
                }
            }
            dp[u][2] = (best_child_influence == INF) ? INF : best_child_influence + C[u];
        }
    }
    if (P[u] == 'Y') {
        dp[u][1] = dp[u][0];
    } else {
        if (is_leaf) {
            dp[u][1] = INF;
        } else {
            long long opt_A = INF;
            long long sum_dp_v0 = 0;
            for (int v : adj[u]) {
                if (v == p) continue;
                sum_dp_v0 += dp[v][0];
            }
            for (int v : adj[u]) {
                if (v == p) continue;
                if (dp[v][2] != INF) {
                    opt_A = min(opt_A, sum_dp_v0 - dp[v][0] + dp[v][2]);
                }
            }
            if (opt_A != INF) opt_A += C[u];

            long long opt_B = INF;
            long long sum_dp_v1 = 0;
            bool possible_B = true;
            for (int v : adj[u]) {
                if (v == p) continue;
                if (dp[v][1] == INF) {
                    possible_B = false;
                    break;
                }
                sum_dp_v1 += dp[v][1];
            }
            if (possible_B) {
                for (int v : adj[u]) {
                    if (v == p) continue;
                    if (dp[v][2] != INF) {
                        opt_B = min(opt_B, sum_dp_v1 - dp[v][1] + dp[v][2]);
                    }
                }
            }
            
            dp[u][1] = min(opt_A, opt_B);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N)) return 0;

    adj.resize(N + 1);
    dp.assign(N + 1, vector<long long>(3, -1));
    C.resize(N + 1);

    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    cin >> P;
    P = " " + P;
    for (int i = 1; i <= N; ++i) {
        cin >> C[i];
    }

    dfs(1, 0);

    cout << dp[1][1] << "\n";

    return 0;
}