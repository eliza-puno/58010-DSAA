#include <iostream>
#include <vector>

int main() {
    int initial_nums[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::vector<int> num(initial_nums, initial_nums + sizeof(initial_nums) / sizeof(int));

    int new_item = 11;
    num.push_back(new_item);

    std::cout << "Original array numbers:";
    for (int i = 0; i < num.size(); ++i) {
        std::cout << " " << num[i];
    }
    std::cout << std::endl;

    return 0;
}

