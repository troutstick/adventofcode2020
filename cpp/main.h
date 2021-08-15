#pragma once

#include <iostream>
#include <fstream>
#include <string>

#include "day1.h"
#include "day2.h"

using namespace std;

const string INPUT_PATH = "./inputs/";

int main();
void readlines(
    const string &filename,
    void (*solver) (vector<string> *)
    );