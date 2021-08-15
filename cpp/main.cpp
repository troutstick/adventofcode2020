#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const string INPUT_PATH = "./inputs/";

int main() {
    ifstream file;
    file.open(INPUT_PATH + "day1.txt");
    cout << file.rdbuf();
    return 0;
}