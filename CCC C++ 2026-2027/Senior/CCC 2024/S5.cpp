#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<long long>> T(2, vector<long long>(N + 1));
    long long total_sum = 0;

    for (int i = 1; i <= N; ++i) {
        cin >> T[0][i];
        total_sum += T[0][i];
    }
    for (int i = 1; i <= N; ++i) {
        cin >> T[1][i];
        total_sum += T[1][i];
    }

    for (int r = 0; r < 2; ++r) {
        for (int i = 1; i <= N; ++i) {
            T[r][i] = T[r][i] * 2 * N - total_sum;
        }
    }

    vector<vector<long long>> P(2, vector<long long>(N + 1, 0));
    for (int r = 0; r < 2; ++r) {
        for (int i = 1; i <= N; ++i) {
            P[r][i] = P[r][i - 1] + T[r][i];
        }
    }

    vector<int> dp0(N + 1, -1e9);
    vector<int> dp1(N + 1, -1e9);
    vector<int> dp2(N + 1, -1e9);

    dp0[0] = 0;

    map<long long, int> max_dp1_by_P1;
    map<long long, int> max_dp2_by_P0;
    map<long long, int> max_dp1_by_negP0;
    map<long long, int> max_dp2_by_negP1;

    for (int i = 1; i <= N; ++i) {
        dp1[i] = max(dp1[i], dp1[i - 1]); 
        dp1[i] = max(dp1[i], dp0[i - 1]); 
        
        if (max_dp1_by_P1.count(P[1][i])) {
            dp1[i] = max(dp1[i], max_dp1_by_P1[P[1][i]] + 1);
        }

        dp2[i] = max(dp2[i], dp2[i - 1]);
        dp2[i] = max(dp2[i], dp0[i - 1]);
        
        if (max_dp2_by_P0.count(P[0][i])) {
            dp2[i] = max(dp2[i], max_dp2_by_P0[P[0][i]] + 1);
        }

        if (P[0][i] + P[1][i] == 0) {
            dp0[i] = max(dp0[i], 1);
        }
        
        if (max_dp1_by_negP0.count(-P[0][i])) {
            dp0[i] = max(dp0[i], max_dp1_by_negP0[-P[0][i]] + 1);
        }
        
        if (max_dp2_by_negP1.count(-P[1][i])) {
            dp0[i] = max(dp0[i], max_dp2_by_negP1[-P[1][i]] + 1);
        }

        if (T[0][i] + T[1][i] == 0) {
            dp0[i] = max(dp0[i], dp0[i - 1] + 1);
        }

        max_dp1_by_P1[P[1][i - 1]] = max(max_dp1_by_P1[P[1][i - 1]], dp1[i]);
        max_dp2_by_P0[P[0][i - 1]] = max(max_dp2_by_P0[P[0][i - 1]], dp2[i]);
        
        max_dp1_by_negP0[P[0][i]] = max(max_dp1_by_negP0[P[0][i]], dp1[i]);
        max_dp2_by_negP1[P[1][i]] = max(max_dp2_by_negP1[P[1][i]], dp2[i]);
    }

    cout << max(0, dp0[N]) << "\n";

    return 0;
}
