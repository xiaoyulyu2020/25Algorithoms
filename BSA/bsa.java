class bsa
{
    public static int binarySearch(int [] nums, int target)
    {
        int left = 0, right = nums.length - 1;

        while (left <= right)
        {
            int mid = (left + right) / 2;
            if(target == nums[mid])
            {
                return mid;
            }
            else if (target < nums[mid])
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

    public static void main(String[] args)
    {
        int [] nums = {1,2,3,4,5,6,7,8};
        int target = 4;
        int index = binarySearch(nums, target);
        if(index != -1)
        {
            System.out.println("Find the number at index " + index);
        }
        else
        {
            System.out.println("Can't find.");
        }
    }
    
}