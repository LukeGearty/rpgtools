#include "ChooseClan.h"

std::string chooseClan(std::mt19937& gen) {
    std::vector<std::string> vampireClans = {
        "Banu Haqim", "Brujah", "Gangrel", "Lasombra", "Ministry", "Hecata", "Malkavian", "Nosferatu", "Ventrue", "Toreador", "Tremere", "Tzimisce", "Ravnos"
    };
    std::uniform_int_distribution<> dist(0, vampireClans.size() - 1);
    return vampireClans[dist(gen)];
}
