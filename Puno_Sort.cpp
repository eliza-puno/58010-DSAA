#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> num = {5, 4, 3, 2, 1};

    std::reverse(num.begin(), num.end());

    std::cout << "Reversed array:";
    for (int i = 0; i < num.size(); ++i) {
        std::cout << " " << num[i];
    }
    std::cout << std::endl;

    return 0;
}

