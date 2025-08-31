#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <unordered_map>


void getCharacters(std::unordered_map<std::string, int>& characters);
void printResults(std::unordered_map<std::string, int>& characters);
int main() {
    std::unordered_map<std::string, int> characters;

    getCharacters(characters);


    printResults(characters);


    return 0;
}

void getCharacters(std::unordered_map<std::string, int>& characters) {

    std::string userInput;


    std::cout << "Enter character names followed by the initiative score\n";
    std::cout << "Ex: Horafrost the Deceiver 22\n";
    std::cout << "Press enter with nothing in it when you are done\n"; //using sentinel value ""

    while (true) {
        std::getline(std::cin, userInput);

        if (userInput.empty()) break;

        std::istringstream iss(userInput);
        std::vector<std::string> tokens;
        std::string word;

        while (iss >> word) tokens.push_back(word);

        if (tokens.size() < 2) {
            std::cout << "Invalid input, try again.\n";
            continue;
        }

        int number = std::stoi(tokens.back());
        tokens.pop_back();

        std::string name;

        for (int i = 0; i < tokens.size(); i++) {
            if (i > 0) {
                name += " ";
            }
            name += tokens[i];
        }

        characters[name] = number;
    }

}

void printResults(std::unordered_map<std::string, int>& characters) {
    std::vector<std::pair<std::string, int>> vec(characters.begin(), characters.end());

    std::sort(vec.begin(), vec.end(), [](const auto& a, const auto& b) {
        return a.second > b.second; // descending
    });

    for (const auto& [name, number] : vec) {
        std::cout << "- " << name << " (" << number << ")\n";
    }


}