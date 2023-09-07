#include <iostream>
#include <vector>

int main() {
    std::vector<int> num;
    num.push_back(5);
    num.push_back(4);
    num.push_back(3);
    num.push_back(2);
    num.push_back(1);

    int x = num.size();
    
    std::cout << x << std::endl;
    
    return 0;
}
