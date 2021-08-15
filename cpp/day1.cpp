#include "day1.h"

using namespace std;

void day1(vector<string> *strs) {
    vector<int> nums;
    unordered_set<int> numset;
    for (string str : *strs) {
        int n = stoi(str);
        nums.push_back(n);
    }

    cout << "the number of nums is " << nums.size() << endl;
    for (int i = 0; i < nums.size(); i++) {
        // if set contains key
        int curr = nums[i];
        int target = 2020 - curr;
        if (numset.find(target) != numset.end()) {
            cout << "The two nums product: ";
            cout << curr * target << endl;
            break;
        } else {
            numset.insert(curr);
        }
    }
    for (int i = 0; i < nums.size() - 1; i++) {
        for (int j = i+1; j < nums.size(); j++) {
            int pair = nums[i] + nums[j];
            int target = 2020 - pair;
            if (numset.find(target) != numset.end()) {
                cout << "The 3 nums: ";
                cout << nums[i] << " " << nums[j] << " " << target << endl;
                cout << "The product: ";
                cout << nums[i] * nums[j] * target << endl;
                return;
            }
        }
    }
}