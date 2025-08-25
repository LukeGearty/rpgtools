#ifndef ATTRIBUTES_H
#define ATTRIBUTES_H

#include <array>
#include <string>
#include <random>

const std::array<std::string, 3> physicalNames = {"Strength", "Dexterity", "Stamina"};
const std::array<std::string, 3> socialNames = {"Charisma", "Manipulation", "Appearance"};
const std::array<std::string, 3> mentalNames = {"Perception", "Intelligence", "Wits"};


struct Attributes {
    std::array<int, 3> physicalTraits; //Strength, Dexterity, Stamina
    std::array<int, 3> socialTraits; //Charisma, Manipulation, Appearance
    std::array<int, 3> mentalTraits; //Perception, Intelligence, Wits    
};


Attributes generateAttributes(std::mt19937& gen);
void printAttributes(const Attributes& a);


#endif