#include "main.h"

int main() {

    readlines("day1.txt", day1);
    readlines("day2.txt", day2);
    readlines("day3.txt", day3);

    return 0;
}

/**
 * Read a file and call a
 * specified solver function on it.
 */
void readlines(const string &filename, void (*solver) (vector<string> *)) {
    ifstream file;
    file.open(INPUT_PATH + filename);

    string str;
    vector<string> *strs = new vector<string>;
    while (getline(file, str)) {
        strs->push_back(str);
    }
    file.close();

    solver(strs);

    delete strs;
}