#include <iostream>
#include <random>
#include <string>
#include <vector>


struct Character {
    std::string race;
    std::string charClass;
    std::array<int, 6> stats; // STR, DEX, CON, INT, WIS, CHA

};


std::string getRandomRace(std::mt19937& gen) {
    std::vector<std::string> races = {
        "Human", "Elf", "Dwarf", "Halfling", "Tiefling", "Half-Orc", "Dragonborn", "Gnome", "Aasimar", "Goliath", "Half-Elf"
    };
    std::uniform_int_distribution<> dist(0, races.size() - 1);
    return races[dist(gen)];
}


std::string getRandomClass(std::mt19937& gen) {
    std::vector<std::string> charClasses = {
        "Bard", "Barbarian", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"
    };
    std::uniform_int_distribution<> dist(0, charClasses.size() - 1);
    return charClasses[dist(gen)];
}


int rollStat(std::mt19937& gen) {
    std::uniform_int_distribution<> d6(1, 6);
    std::vector<int> rolls;

    for (int i = 0; i < 4; i++) {
        rolls.push_back(d6(gen));
    }

    std::sort(rolls.begin(), rolls.end());//sort lowest to highest
    return rolls[1] + rolls[2] + rolls[3]; 
}


std::array<int,6> generateStats(std::mt19937& gen) {
    std::array<int,6> stats;
    for (int i = 0; i < 6; i++) {
        stats[i] = rollStat(gen);
    }
    return stats;
}


struct Character createCharacter(std::mt19937& gen) {

    struct Character c;
    c.race = getRandomRace(gen);
    c.charClass = getRandomClass(gen);
    c.stats = generateStats(gen);

    return c;
    
}

void printCharacter(struct Character& c) {
    std::vector<std::string> stats = {
        "STR", "DEX", "CON", "INT", "WIS", "CHA"
    };

    std::cout << c.race << " " << c.charClass << '\n';

    for (int i = 0; i < stats.size(); i++) {
        std::cout << stats[i] << " " << c.stats[i] << '\n';
    }

    std::cout << std::endl;
}


int main() {
    std::random_device rd; // Non-deterministic seed. A random seed
    std::mt19937 gen(rd()); // Mersenne Twister RNG 

    struct Character c = createCharacter(gen);

    printCharacter(c);



    return 0;
}