#include "Attributes.h"
#include <iostream>


struct Priority {
    //priorities are based on 7 / 5 / 3 dots to each attribute
    std::string name; //the name of the attribute
    std::array<int, 3>* values; //the actual attribute array

};


void distributeDots(std::array<int, 3>& attributes, int extraDots, std::mt19937& gen) {

    for (int i = 0; i < 3; i++) attributes[i] = 1;

    std::uniform_int_distribution<> dist(0, 2);

    for (int i = 0; i < extraDots; i++) {
        int idx = dist(gen);
        if (attributes[idx] < 5) {
            attributes[idx]++;
        } else {
            i--;
        }
    }
}


Attributes generateAttributes(std::mt19937& gen) {
    Attributes a;

    std::vector<Priority> priorities = {
        {"Physical", &a.physicalTraits},
        {"Social", &a.socialTraits},
        {"Mental", &a.mentalTraits}
    };

    std::shuffle(priorities.begin(), priorities.end(), gen);

    std::array<int, 3> priorityNums = {7, 5, 3};

    for (int i = 0; i < 3; i++) {
        distributeDots(*priorities[i].values, priorityNums[i], gen);
        //baseline already counts as 3 dots
    }

    return a;
}


void printAttributes(const Attributes& a) {
    std::cout << "Physical:\n";
    for (int i = 0; i < 3; i++) {
        std::cout << " " << physicalNames[i] << ": " << a.physicalTraits[i] << "\n";
    }

    std::cout << "Social:\n";
    for (int i = 0; i < 3; i++) {
        std::cout << " " << socialNames[i] << ": " << a.socialTraits[i] << "\n";
    }

    std::cout << "Mental:\n";
    for (int i = 0; i < 3; i++) {
        std::cout << " " << mentalNames[i] << ": " << a.mentalTraits[i] << "\n";
    }
}