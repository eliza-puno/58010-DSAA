#include <iostream>

using namespace std;

int main()
{
    int num[] = {1,2,3,4,5,6,7,8,9,10};
    int i;
    int n = 9;
    cout<<"Traversal Algorithm:"<<endl;
    for(int i=0;i<=n;i++)
    {
          cout<<"num["<<i<<"]="<<num[i]<<endl;
    }
    return 0;
}
