#include <iostream>
#include <limits> // for std::numeric_limits

void vulnerableFunction() {
    int largeNumber = std::numeric_limits<int>::max() / 2 + 1; // A large number close to the max value of int
    int result = largeNumber * 2; // This will cause an overflow
    std::cout << "Vulnerable Result: " << result << std::endl; // This will not show the correct value due to overflow
}

int main() {
    std::cout << "Demonstrating CWE-190 Integer Overflow" << std::endl;
    vulnerableFunction();
    return 0;
}
