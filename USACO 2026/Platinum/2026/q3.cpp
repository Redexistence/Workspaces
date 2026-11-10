#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Clue {
    char v;
    long long r, c;
};

// Counts integers x in [L, U] such that (X & 1) == parity (0 for even, 1 for odd)
long long count_parity(long long L, long long U, int parity) {
    if ((L & 1) != parity) L++;
    if ((U & 1) != parity) U--;
    if (L > U) return 0;
    return (U - L) / 2 + 1;
}

long long solve_family(long long min_D, long long max_D, const vector<Clue>& clues, bool anti) {
    if (min_D > max_D) return 0;
    long long L_even = min_D, U_even = max_D;
    long long L_odd = min_D, U_odd = max_D;

    for (const auto& clue : clues) {
        long long s = anti ? (clue.r + clue.c) : (clue.r - clue.c);
        int s_par = (s & 1);
        bool is_plus = (clue.v == '+');

        // For even D: D >= s iff (plus && s even) || (minus && s odd)
        if ((is_plus && s_par == 0) || (!is_plus && s_par == 1)) {
            L_even = max(L_even, s);
        } else {
            U_even = min(U_even, s - 1);
        }

        // For odd D: D >= s iff (plus && s odd) || (minus && s even)
        if ((is_plus && s_par == 1) || (!is_plus && s_par == 0)) {
            L_odd = max(L_odd, s);
        } else {
            U_odd = min(U_odd, s - 1);
        }
    }

    return count_parity(L_even, U_even, 0) + count_parity(L_odd, U_odd, 1);
}

void solve() {
    long long R, C;
    int X;
    if (!(cin >> R >> C >> X)) return;

    vector<Clue> clues(X);
    bool all_plus = true;
    for (int i = 0; i < X; i++){
        cin >> clues[i].v >> clues[i].r >> clues[i].c;
        if (clues[i].v != '+') all_plus = false;
    }

    // 1. Anti-diagonal family: D in [0, R + C - 1]
    long long ans = solve_family(0, R + C - 1, clues, true);

        // 2. Main-diagonal family (only distinct when R >= 2 and C >= 2): D in [1 - C, R - 2]
    if (R >= 2 && C >= 2) {
        ans += solve_family(1 - C, R - 2, clues, false);
    }

    // 3. Special all-'+' 2x2 grid
    if (R == 2 && C == 2 && all_plus) {
        ans += 1;
    }

    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}