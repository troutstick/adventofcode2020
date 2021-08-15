#include "day2.h"
#include "utils.h"
#include <stdexcept>

void day2(vector<string> *input) {
    int num_valid1 = 0;
    int num_valid2 = 0;
    string delimiter = ": ";
    for (string s : *input) {
        vector<string> *splits = split(s, delimiter);
        if (splits->size() != 2) {
            throw runtime_error("splitter should have split into two strings");
        }
        string pw_policy = (*splits)[0];
        vector<string> *policies = split(pw_policy, " ");
        vector<string> *min_and_max = split((*policies)[0], "-");
        
        char ch = (*policies)[1].at(0);
        int min = stoi((*min_and_max)[0]);
        int max = stoi((*min_and_max)[1]);
        string pw = (*splits)[1];

        int ch_count = count(pw.begin(), pw.end(), ch);
        if (min <= ch_count && max >= ch_count) {
            num_valid1++;
        }

        if ((pw.at(min-1) == ch) != (pw.at(max-1) == ch)) {
            num_valid2++;
        }

        delete splits;
        delete policies;
        delete min_and_max;
    }

    cout << "The answer for Day 2 Part 1 is " << num_valid1 << endl;
    cout << "The answer for Day 2 Part 2 is " << num_valid2 << endl;

}