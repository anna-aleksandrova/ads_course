#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>

using namespace std;

int sign(int x) {
    if (x > 0) return 1;
    if (x < 0) return -1;
    return 0;
}

class SegmentTree {
public:
    int size;
    vector<int> items;

    SegmentTree(const vector<int>& array) {
        int n = 1 << ((int)log2(array.size() - 1) + 1);
        size = n;
        items.assign(2 * n, 1);

        for (int i = 0; i < array.size(); ++i) {
            items[n + i] = sign(array[i]);
        }

        for (int i = n - 1; i > 0; --i) {
            items[i] = items[2 * i] * items[2 * i + 1];
        }
    }

    void update(int pos, int x) {
        pos += size;
        items[pos] = sign(x);
        for (int i = pos / 2; i > 0; i /= 2) {
            items[i] = items[2 * i] * items[2 * i + 1];
        }
    }

    int prod(int left, int right) {
        left += size;
        right += size;
        int res = 1;
        while (left <= right) {
            if (left % 2 == 1) res *= items[left++];
            if (right % 2 == 0) res *= items[right--];
            if (res == 0) return 0;
            left /= 2;
            right /= 2;
        }
        return res;
    }
};

int main() {
    ifstream fin("input.txt");
    string line;

    while (getline(fin, line)) {
        if (line.empty()) continue;

        int n, k;
        sscanf(line.c_str(), "%d %d", &n, &k);

        vector<int> array(n);
        for (int i = 0; i < n; ++i) {
            fin >> array[i];
        }

        SegmentTree st(array);
        for (int i = 0; i < k; ++i) {
            char cmd;
            int a, b;
            fin >> cmd >> a >> b;
            if (cmd == 'P') {
                int res = st.prod(a - 1, b - 1);
                if (res == 0) cout << "0";
                else if (res > 0) cout << "+";
                else cout << "-";
            } else if (cmd == 'C') {
                st.update(a - 1, b);
            }
        }
        cout << endl;
        getline(fin, line);
    }

    return 0;
}
