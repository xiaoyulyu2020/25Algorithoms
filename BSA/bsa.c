#include <stdio.h>

int binarysearch(int nums[], int n, int target)
{

    int left = 0;
    int right = n - 1;
    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (nums[mid] == target)
        {
            return target;
        }
        else if (nums[mid] >= target)
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

int main(void)
{
    int nums[] = {1, 2, 3, 4, 5, 6, 7, 8};
    int target = 4;
    size_t n = sizeof nums / sizeof *nums;
    int index = binarysearch(nums, n, target);
    if (index != -1)
    {
        printf("find it at index %d", index - 1);
    }
    else
    {
        printf("Can't find it");
    }
    return 1;
}
