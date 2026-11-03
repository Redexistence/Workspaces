#include <iostream>
#include <vector>

using namespace std;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= 1000000007;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % 1000000007;
        base = (base * base) % 1000000007;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, 1000000005);
}

struct CoachState {
    long long pos;
    long long stored_val;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long d;
    if (!(cin >> n >> d)) return 0;

    vector<long long> p(n);
    vector<int> o(n);

    for (int i = 0; i < n; i++) {
        cin >> p[i] >> o[i];
    }

    long long MOD = 1000000007;
    long long inv2 = modInverse(2);

    long long inactive_sum = 0;
    long long active_base_sum = 1;
    long long G = 1;              
    long long G_inv = 1;          

    vector<CoachState> active_coaches;
    // Push the initial state (-1 means no coach selected yet)
    active_coaches.push_back({-1, 1}); 

    int next_inactive_idx = 0; // Pointer to the oldest active coach

    for (int i = 0; i < n; i++) {
        if (o[i] == 1) {
            // Total current valid combinations
            long long S = (inactive_sum + (active_base_sum * G) % MOD) % MOD;
            // Scale by G_inv so it accurately reflects future global multiplications
            long long stored_val = (S * G_inv) % MOD;
            
            active_coaches.push_back({p[i], stored_val});
            active_base_sum = (active_base_sum + stored_val) % MOD;
        } else {
            // Slide window: move coaches that are too far to the left into inactive_sum
            while (next_inactive_idx < active_coaches.size()) {
                if (active_coaches[next_inactive_idx].pos != -1 && p[i] - active_coaches[next_inactive_idx].pos > d) {
                    long long actual_val = (active_coaches[next_inactive_idx].stored_val * G) % MOD;
                    inactive_sum = (inactive_sum + actual_val) % MOD;
                    active_base_sum = (active_base_sum - active_coaches[next_inactive_idx].stored_val + MOD) % MOD;
                    next_inactive_idx++;
                } else if (active_coaches[next_inactive_idx].pos == -1) {
                    // State -1 can never satisfy any camper, so it immediately becomes inactive
                    long long actual_val = (active_coaches[next_inactive_idx].stored_val * G) % MOD;
                    inactive_sum = (inactive_sum + actual_val) % MOD;
                    active_base_sum = (active_base_sum - active_coaches[next_inactive_idx].stored_val + MOD) % MOD;
                    next_inactive_idx++;
                } else {
                    break;
                }
            }

            // All remaining active states are in D units, choices double
            G = (G * 2) % MOD;
            G_inv = (G_inv * inv2) % MOD;
        }
    }

    // Compute total subsets (including the empty subset)
    long long final_S = (inactive_sum + (active_base_sum * G) % MOD) % MOD;
    // Subtract 1 to exclude the empty subset as required
    long long ans = (final_S - 1 + MOD) % MOD;

    cout << ans << "\n";

    return 0;
}