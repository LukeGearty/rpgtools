#include "Attributes.h"
#include "ChooseClan.h"
#include <random>



//Uses V20 rules to create the vampire character
struct VampireCharacter {
    std::string vampireClan;
    Attributes attributes;
};


struct VampireCharacter createCharacter(std::string vampireClan, Attributes attributes, std::mt19937& gen) {
    Attributes a = generateAttributes(gen);
    std::string vClan = chooseClan(gen);
    struct VampireCharacter vCharacter;
    vCharacter.vampireClan = vClan;
    vCharacter.attributes = a;

    return vCharacter;

}

int main() {

    std::random_device rd;
    std::mt19937 gen(rd());


    




    return 0;
}