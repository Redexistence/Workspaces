#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Event {
    int x, y, id;
    bool is_start;
    bool operator<(const Event& other) const {
        if (x != other.x) return x < other.x;
        if (y != other.y) return y < other.y;
        return is_start < other.is_start; 
    }
};

struct Board {
    int x1, y1, x2, y2;
    int savings;
};

struct BIT {
    int size;
    vector<int> tree;
    BIT(int n) : size(n), tree(n + 1, 0) {}
    
    void update(int idx, int val) {
        for (; idx <= size; idx += idx & -idx) {
            tree[idx] = max(tree[idx], val);
        }
    }
    
    int query(int idx) {
        int res = 0;
        for (; idx > 0; idx -= idx & -idx) {
            res = max(res, tree[idx]);
        }
        return res;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    freopen("boards.in", "r", stdin);
    freopen("boards.out", "w", stdout);

    int N, P;
    if (!(cin >> N >> P)) return 0;

    vector<Board> boards(P);
    vector<Event> events;
    vector<int> y_coords;

    for (int i = 0; i < P; ++i) {
        cin >> boards[i].x1 >> boards[i].y1 >> boards[i].x2 >> boards[i].y2;
        boards[i].savings = (boards[i].x2 - boards[i].x1) + (boards[i].y2 - boards[i].y1);
        
        events.push_back({boards[i].x1, boards[i].y1, i, true});
        events.push_back({boards[i].x2, boards[i].y2, i, false});
        
        y_coords.push_back(boards[i].y1);
        y_coords.push_back(boards[i].y2);
    }

    sort(y_coords.begin(), y_coords.end());
    y_coords.erase(unique(y_coords.begin(), y_coords.end()), y_coords.end());
    auto get_y_idx = [&](int y) {
        return lower_bound(y_coords.begin(), y_coords.end(), y) - y_coords.begin() + 1;
    };

    sort(events.begin(), events.end());

    BIT bit(y_coords.size());
    vector<int> dp(P, 0);
    int max_total_savings = 0;

    for (const auto& ev : events) {
        int y_idx = get_y_idx(ev.y);
        if (ev.is_start) {
            dp[ev.id] = bit.query(y_idx) + boards[ev.id].savings;
            max_total_savings = max(max_total_savings, dp[ev.id]);
        } else {
            bit.update(y_idx, dp[ev.id]);
        }
    }

    long long total_walk = 2LL * N - max_total_savings;
    cout << total_walk << "\n";

    return 0;
}
