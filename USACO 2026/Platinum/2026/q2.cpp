#include <bits/stdc++.h>
using namespace std;
// time complexity is O(100Q)
vector<long long> inv(long long n) {
    vector<long long> ans;
    ans.push_back(4000000000000000000);
    for(int i = 0; i < 111; i++) {
        ans.push_back(n);
        n = (2 * n + 4) / 3 - 2;
    }
    return ans;
}

int main() {
    int q;
    cin >> q;
    while (q--) {
        long long l1, r1, l2, r2, t;
        cin >> l1 >> r1 >> l2 >> r2 >> t;

        long long ans = 0;
        vector<long long> inv1 = inv(t-1);
        vector<long long> inv2 = inv(l2+t-1);
        vector<long long> inv3 = inv(r2+t);
        for (int j = 1l; j < 111; j++) {
            // l1 <= i <= min(t/2,r1)
            // 3*i-1 <= min(inv1[j-1],inv3[j])
            // 3*i-1 > inv2[j]
            long long low = max(l1, (inv2[j]+4)/3);
            long long high = min(min(t/2,r1),(min(inv1[j-1],inv3[j])+4)/3-1);
            ans += max(0LL, high-low+1);
        }

        // l1 <= i <= r1
        // l2 <= i <= r2
        // t <= 2*i-1
        ans += max(0LL, min(r1,r2)-max(max(l1,l2),t/2+1)+1);
        cout << ans << endl;
    }
}