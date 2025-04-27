#include <iostream>
#include <vector>

using namespace std;

const int MAXN = 256;

class SegmentTree {
    vector<long long> tree, lazy;
    int n;

public:
    SegmentTree(int size) {
        n = size;
        tree.resize(4 * n);
        lazy.resize(4 * n);
    }

    void push(int v, int l, int r) {
        if (lazy[v] != 0) {
            tree[v] += lazy[v] * (r - l + 1);
            if (l != r) {
                lazy[v * 2] += lazy[v];
                lazy[v * 2 + 1] += lazy[v];
            }
            lazy[v] = 0;
        }
    }

    void range_add(int v, int l, int r, int ql, int qr, int val) {
        push(v, l, r);
        if (qr < l || r < ql)
            return;
        if (ql <= l && r <= qr) {
            lazy[v] += val;
            push(v, l, r);
            return;
        }
        int m = (l + r) / 2;
        range_add(v * 2, l, m, ql, qr, val);
        range_add(v * 2 + 1, m + 1, r, ql, qr, val);
        tree[v] = tree[v * 2] + tree[v * 2 + 1];
    }

    long long range_sum(int v, int l, int r, int ql, int qr) {
        push(v, l, r);
        if (qr < l || r < ql)
            return 0;
        if (ql <= l && r <= qr)
            return tree[v];
        int m = (l + r) / 2;
        return range_sum(v * 2, l, m, ql, qr) + range_sum(v * 2 + 1, m + 1, r, ql, qr);
    }

    void add(int l, int r, int val) {
        range_add(1, 0, n - 1, l, r, val);
    }

    long long get_sum(int l, int r) {
        return range_sum(1, 0, n - 1, l, r);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q, L, R, p;
    cin >> q >> L >> R >> p;

    SegmentTree seg(MAXN);

    for (int i = 0; i < q; ++i) {
        int l = min(L, R);
        int r = max(L, R);
        seg.add(l, r, 1);
        long long s = seg.get_sum(l, r);
        L = s % p;
        R = 255 - (s % p);
    }

    cout << seg.get_sum(0, 255) << "\n";

    return 0;
}