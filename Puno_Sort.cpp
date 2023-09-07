#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int arr[] = {5, 4, 3, 2, 1};
    std::vector<int> num(arr, arr + sizeof(arr) / sizeof(arr[0]));

    std::reverse(num.begin(), num.end());

    std::cout << "Reversed array:";
    for (std::vector<int>::iterator it = num.begin(); it != num.end(); ++it) {
        std::cout << " " << *it;
    }
    std::cout << std::endl;

    return 0;
}

