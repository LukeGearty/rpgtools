#include <iostream>
#include <random>


// Testing the randomness of std::random_device
int main() {

    std::random_device rd;
    std::cout << "Testing std::random_device...\n";
    for (int i = 0; i < 10; i++) {
        std::cout << rd() << "\n";
    }

    return 0;
}