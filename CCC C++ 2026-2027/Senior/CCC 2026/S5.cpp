#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

ll solve_case(ll N, ll M, ll K, ll R, ll C) {
    if (N < 3 || M < 3 || K < 4) return 0;

    const ll H = N - 2, W = M - 2;

    struct Connection {
        ll added; // extra fence cells beyond the rectangle boundary
        ll lost;  // rectangular inside cells consumed by that connection
    };

    // Return the cheapest way to include (R,C), for an h by w rectangular
    // interior.  The rectangle's top-left outer-cell coordinates are (a,b).
    auto extra = [&](ll h, ll w) -> Connection {
        const ll INF = (ll)4e18;
        if (h < 1 || h > H || w < 1 || w > W) return {INF, INF};

        vector<ll> as = {1, N - h - 1, R - h - 1, R - h, R - 1, R};
        vector<ll> bs = {1, M - w - 1, C - w - 1, C - w, C - 1, C};
        Connection best{INF, INF};

        for (ll a0 : as) {
            if (a0 < 1 || a0 > N - h - 1) continue;
            for (ll b0 : bs) {
                if (b0 < 1 || b0 > M - w - 1) continue;

                ll top = a0, bottom = a0 + h + 1;
                ll left = b0, right = b0 + w + 1;
                ll d = 0;

                if (R < top) d += top - R;
                else if (R > bottom) d += R - bottom;
                if (C < left) d += left - C;
                else if (C > right) d += C - right;

                Connection candidate;
                if (d == 0) {
                    if (R == top || R == bottom || C == left || C == right)
                        candidate = {0, 0};
                    else {
                        ll to_side = min({R - top - 1, bottom - R - 1,
                                          C - left - 1, right - C - 1});
                        // The path lies inside the rectangle. It consumes
                        // interior cells, but adds no fence cells outside
                        // the rectangle boundary.
                        candidate = {0, to_side + 1};
                    }
                } else {
                    candidate = {d, 0};
                }

                // The connection consumes both outside path cells and
                // inside path cells from the K-cell limit.  Minimize the
                // total added amount, not just the number outside the
                // rectangle.
                if (candidate.added + candidate.lost <
                        best.added + best.lost ||
                    (candidate.added + candidate.lost ==
                         best.added + best.lost &&
                     candidate.lost < best.lost))
                    best = candidate;
            }
        }
        return best;
    };

    vector<ll> hs = {1, H, R - 3, R - 2, R - 1, R,
                     N - R - 2, N - R - 1, N - R,
                     (K - 4) / 4};
    vector<ll> ws = {1, W, C - 3, C - 2, C - 1, C,
                     M - C - 2, M - C - 1, M - C,
                     (K - 4) / 4};

    // The cost is monotone in w for fixed h: increasing w adds two fence
    // cells, while the shortest connection can remove at most one cell of
    // cost.  Therefore, for every relevant h, binary-search the largest
    // affordable w instead of sampling only a few widths.
    vector<ll> hc = hs, wc = ws;
    auto add_neighbourhood = [](vector<ll>& v, ll x) {
        for (ll d = -4; d <= 4; ++d) v.push_back(x + d);
    };

    // Between structural breakpoints, the cost has the form
    //     a*h + b*w + constant.
    // On this line, h*w is maximized at
    //     h = q/(2*a), w = q/(2*b),
    // not at q*b/(a+b) and q*a/(a+b).  The latter is the point where
    // h and w have a prescribed ratio, and misses the optimum whenever
    // a != b.
    const ll q = K - 4;
    for (ll a = 1; a <= 3; ++a) {
        for (ll b = 1; b <= 3; ++b) {
            add_neighbourhood(hc, q / (2 * a));
            add_neighbourhood(wc, q / (2 * b));
        }
    }

    // Also include the corresponding points after subtracting the constant
    // offsets introduced by the required cell's row and column.
    // Every distance from (R,C) to a possible side of a rectangle is one
    // of these values, up to the dimension-dependent term.  Include all
    // sums of a row term and a column term; using only R, N-R, C and M-C
    // misses the one-cell offset caused by the boundary itself.
    // Collect every constant that can occur when a side of the rectangle
    // passes the required cell or an outer edge.  The earlier list omitted
    // the zero/one-cell variants on the opposite sides; those omissions can
    // move the optimum far enough to be missed by the sampled search.
    vector<ll> row_offsets = {
        0, 1, 2, R - 3, R - 2, R - 1, R,
        N - R - 2, N - R - 1, N - R,
        N - 2, N - 1
    };
    vector<ll> col_offsets = {
        0, 1, 2, C - 3, C - 2, C - 1, C,
        M - C - 2, M - C - 1, M - C,
        M - 2, M - 1
    };
    vector<ll> offsets;
    for (ll x : row_offsets)
        for (ll y : col_offsets)
            offsets.push_back(x + y);

    for (ll x : offsets) {
        for (ll remaining : {q - x, q + x}) {
            if (remaining < 0) continue;
            for (ll a = 1; a <= 3; ++a) {
                for (ll b = 1; b <= 3; ++b) {
                    add_neighbourhood(hc, remaining / (2 * a));
                    add_neighbourhood(wc, remaining / (2 * b));
                }
            }
        }
    }

    for (ll x : hs) add_neighbourhood(hc, x);
    for (ll x : ws) add_neighbourhood(wc, x);

    ll answer = 0;
    auto cost_of = [&](ll h, ll w) -> ll {
        Connection e = extra(h, w);
        if (e.added >= (ll)3e18 || e.lost >= (ll)3e18)
            return (ll)4e18;
        // Both outside path cells and cells removed from the interior are
        // selected fence cells, so both count against K.
        return 2 * h + 2 * w + 4 + e.added + e.lost;
    };

    // The cheapest connection is not necessarily the best connection for the
    // answer.  For example, a connection that costs one extra cell may avoid
    // losing several cells from the rectangle's interior.  Enumerate every
    // relevant rectangle placement and choose the best one that fits.
    auto best_lost = [&](ll h, ll w, ll extra_budget) -> ll {
        if (h < 1 || h > H || w < 1 || w > W) return -1;

        const ll INF = (ll)4e18;
        vector<ll> as = {1, N - h - 1, R - h - 1, R - h, R - 1, R};
        vector<ll> bs = {1, M - w - 1, C - w - 1, C - w, C - 1, C};
        ll answer_lost = INF;

        for (ll a0 : as) {
            if (a0 < 1 || a0 > N - h - 1) continue;
            for (ll b0 : bs) {
                if (b0 < 1 || b0 > M - w - 1) continue;

                ll top = a0, bottom = a0 + h + 1;
                ll left = b0, right = b0 + w + 1;
                ll d = 0;
                if (R < top) d += top - R;
                else if (R > bottom) d += R - bottom;
                if (C < left) d += left - C;
                else if (C > right) d += C - right;
                ll lost = 0;
                if (d == 0 &&
                    !(R == top || R == bottom || C == left || C == right)) {
                    ll to_side = min({R - top - 1, bottom - R - 1,
                                      C - left - 1, right - C - 1});
                    lost = to_side + 1;
                }

                // Cells used by an inside connection are fence cells too.
                // They therefore consume the same K budget as an outside
                // connection, even though they reduce the enclosed area.
                if (d + lost > extra_budget) continue;
                answer_lost = min(answer_lost, lost);
            }
        }
        return answer_lost == INF ? -1 : answer_lost;
    };

    auto consider = [&](ll h, ll w) {
        if (h < 1 || h > H || w < 1 || w > W) return;
        ll budget = K - (2 * h + 2 * w + 4);
        if (budget < 0) return;
        ll lost = best_lost(h, w, budget);
        if (lost >= 0) answer = max(answer, h * w - lost);
    };

    // The small/medium subtask is cheap enough to solve exactly.  This is
    // also important because affordability is not guaranteed to be monotone
    // in a dimension: an extra column can place (R,C) on the boundary and
    // remove the interior connection cost.  Binary-searching such a function
    // can skip the optimum.
    // Solve the complete N,M <= 2000 subtask exactly.  The large-case
    // candidate search below is not suitable for this range: the objective
    // can change at a rectangle placement breakpoint, and those breakpoints
    // are not all stationary points of the budget equation.
    if (N <= 2000 && M <= 2000) {
        for (ll h = 1; h <= H; ++h)
            for (ll w = 1; w <= W; ++w)
                consider(h, w);
        return answer;
    }
    for (ll h : hc) {
        if (h < 1 || h > H) continue;

        ll lo = 0, hi = W + 1;
        while (hi - lo > 1) {
            ll mid = lo + (hi - lo) / 2;
            if (cost_of(h, mid) <= K) lo = mid;
            else hi = mid;
        }
        for (ll d = -4; d <= 4; ++d) consider(h, lo + d);
        for (ll w : wc) consider(h, w);
    }

    // Symmetric search: this also catches optima whose height, rather than
    // width, is the dimension determined by the budget.
    for (ll w : wc) {
        if (w < 1 || w > W) continue;
        ll lo = 0, hi = H + 1;
        while (hi - lo > 1) {
            ll mid = lo + (hi - lo) / 2;
            if (cost_of(mid, w) <= K) lo = mid;
            else hi = mid;
        }
        for (ll d = -4; d <= 4; ++d) consider(lo + d, w);
    }

    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        ll N, M, K, R, C;
        cin >> N >> M >> K >> R >> C;
        cout << solve_case(N, M, K, R, C) << '\n';
    }
}
