#include <iostream>
#include <random>

int main() {

    std::random_device rd;
    std::mt19937 gen(rd());

    std::uniform_int_distribution<> d20(1, 20);


    for (int i = 0; i < 10; i++) {
        std::cout << d20(gen) << " ";
    }


    return 0;
}