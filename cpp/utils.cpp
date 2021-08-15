#include "utils.h"

/**
 * Return a heap allocated vector of strings
 * made by splitting an input string.
 */
vector<string> *split(string s, string delimiter) {

    vector<string> *split_strings = new vector<string>{};

    int start = 0;
    int end = s.find(delimiter);
    while (end != -1) {
        split_strings->push_back(s.substr(start, end-start));
        start = end + delimiter.size();
        end = s.find(delimiter, start);
    }
    split_strings->push_back(s.substr(start, end-start));
    
    return split_strings;
}