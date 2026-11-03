#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>

using namespace std;

struct Point {
    long long x, y;
    long long weight;
};

// Returns the quadrant (1 to 4) of a point for radial sorting
int quadrant(const Point& p) {
    if (p.x > 0 && p.y >= 0) return 1;
    if (p.x <= 0 && p.y > 0) return 2;
    if (p.x < 0 && p.y <= 0) return 3;
    if (p.x >= 0 && p.y < 0) return 4;
    return 0;
}

// Computes 2D cross product
long long cross_product(const Point& a, const Point& b) {
    return a.x * b.y - a.y * b.x;
}

// Counter-clockwise angular sort
bool compare_points(const Point& a, const Point& b) {
    int q1 = quadrant(a);
    int q2 = quadrant(b);
    if (q1 != q2) return q1 < q2;
    return cross_product(a, b) > 0;
}

void solve() {
    int N;
    if (!(cin >> N)) return;

    map<pair<long long, long long>, long long> group_counts;
    long long M = 0; // Total count of valid non-zero cows

    for (int i = 0; i < N; ++i) {
        long long h, p, s;
        cin >> h >> p >> s;
        long long x = 2 * h - p - s;
        long long y = 2 * p - h - s;
        
        if (x == 0 && y == 0) continue; // Always ties, safely exclude
        
        long long g = std::gcd(std::abs(x), std::abs(y));
        x /= g;
        y /= g;
        group_counts[{x, y}]++;
        M++;
    }

    if (M < 3) {
        cout << 0 << "\n";
        return;
    }

    vector<Point> groups;
    for (auto const& [coord, count] : group_counts) {
        groups.push_back({coord.first, coord.second, count});
    }

    int m = groups.size();

    // Sort unique strategy groups angularly counter-clockwise
    sort(groups.begin(), groups.end(), compare_points);

    long long non_containing = 0;

    // Type 1 & Type 2: Triples where at least 2 cows share the same direction group
    for (int i = 0; i < m; ++i) {
        long long w = groups[i].weight;
        if (w >= 3) {
            non_containing += (w * (w - 1) * (w - 2)) / 6;
        }
        if (w >= 2) {
            non_containing += (w * (w - 1) / 2) * (M - w);
        }
    }

    // Type 3: Triples from 3 distinct groups lying within a <= 180-degree semi-circle
    int R = 0;
    long long S1 = 0; // Sum of weights in the active window
    long long S2 = 0; // Sum of squared weights in the active window

    for (int i = 0; i < m; ++i) {
        if (R <= i) {
            R = i + 1;
            S1 = 0;
            S2 = 0;
        }
        
        // Expand window while the next group is within <= 180 degrees counter-clockwise
        while (R < i + m) {
            int idx = R % m;
            long long cp = cross_product(groups[i], groups[idx]);
            long long dp = groups[i].x * groups[idx].x + groups[i].y * groups[idx].y;
            
            if (cp > 0 || (cp == 0 && dp < 0)) {
                long long w = groups[idx].weight;
                S1 += w;
                S2 += w * w;
                R++;
            } else {
                break;
            }
        }

        // Distinct pairs sum inside the window = (S1^2 - S2) / 2
        long long pairs_sum = (S1 * S1 - S2) / 2;
        non_containing += groups[i].weight * pairs_sum;

        // Slide the window out: pop the next element out of the current running sums
        if (R > i + 1) {
            long long w_next = groups[(i + 1) % m].weight;
            S1 -= w_next;
            S2 -= w_next * w_next;
        }
    }

    // Total combinations of picking any 3 valid non-zero cows
    long long total_triples = (M * (M - 1) * (M - 2)) / 6;
    long long cyclic_triples = total_triples - non_containing;

    cout << cyclic_triples << "\n";
}

int main() {
    // Maximize stream optimization for USACO Platinum speed standards
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int T;
    if (cin >> T) {
        while (T--) {
            solve();
        }
    }
    return 0;
}