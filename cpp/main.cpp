#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

const string INPUT_PATH = "./inputs/";

int main() {
    ifstream file;
    file.open(INPUT_PATH + "day1.txt");
    string str;
    vector<int> nums;
    unordered_set<int> numset;
    while (getline(file, str)) {
        int n = stoi(str);
        nums.push_back(n);
    }
    cout << "the number of nums is " << nums.size() << endl;
    for (int i = 0; i < nums.size(); i++) {
        // if set contains key
        int curr = nums[i];
        int target = 2020 - curr;
        if (numset.find(target) != numset.end()) {
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
                cout << nums[i] << " " << nums[j] << " " << target << endl;
                cout << nums[i] * nums[j] * target << endl;
                return 0;
            }
        }
    }
    return 0;
}