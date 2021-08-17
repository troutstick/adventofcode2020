#include "day3.h"
#include "utils.h"

const int INDICES_LEN = 5;
const int go_right_by[INDICES_LEN] = {1,3,5,7,1};

inline int increment(int n, int increment, int mod) {
    return (n+increment) % mod;
}

inline void check_tree(string *tree_str, int *indices, int *num_trees, int i, int mod) {
    if ((*tree_str)[indices[i]] == '#') {
        num_trees[i]++;
    }
    indices[i] = increment(indices[i], go_right_by[i], mod);
}

void day3(vector<string> *input) {
    int mod = (*input)[0].length();
    int indices[INDICES_LEN] = {0};
    int num_trees[INDICES_LEN] = {0};
    bool flag = true;
    for (string s : *input) {
        for (int i = 0; i < INDICES_LEN-1; i++) {
            check_tree(&s, indices, num_trees, i, mod);
        }
        if (flag) {
            check_tree(&s, indices, num_trees, 4, mod);
        }
        flag = !flag;
	}
    long p2 = 1;
    for (int i = 0; i < INDICES_LEN;i++) {
        p2 *= num_trees[i];
    }
    cout << "Day 3 Part 1: There are " << num_trees[1] << " trees." << endl;
    cout << "Day 3 Part 2: There are " << p2 << " multiplied trees." << endl;
}
