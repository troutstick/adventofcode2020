#include "main.h"

int main() {
    day1(readlines("day1.txt"));
    day2(readlines("day2.txt"));
    return 0;
}

/* Return a heap allocated string. */
vector<string> *readlines(const string &filename) {
    ifstream file;
    file.open(INPUT_PATH + filename);

    string str;
    vector<string> *strs = new vector<string>;
    while (getline(file, str)) {
        strs->push_back(str);
    }
    file.close();

    return strs;
}