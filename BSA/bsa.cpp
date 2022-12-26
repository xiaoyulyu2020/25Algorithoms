#include <iostream>

int bsa(int num [], int starge, int ln)
{
    int left = 0;
    int right = ln - 1;
    while (left <= right)
    {
        int mid = (left + right) / 2;
        if(num[mid] == right)
        {
            return mid;
        }
        else if (num[mid] > right)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    return -1;
}


int main()
{
    int nums[] = {1,2,3,4,5,6,7};
    int ln = sizeof nums / sizeof *nums;
    int target = 5;
    int index = bsa(nums, target, ln);
    if(index != -1)
    {
        std::cout<<"Find de num at index "<< index - 1 << std::endl;
    }
    else
    {
        std::cout << "Can't Find num." << std::endl;
    }
}