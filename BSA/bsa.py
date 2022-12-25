def search (num , ls):
    # search range from (first ... right)
    (left, right) = (0, len(ls)-1)
    
    #left always smaller than right, keep search.
    while left <= right:
        # middle index
        mid = (left + right)//2
        
        if ls[mid] == num:
            return mid
        elif ls[mid] >= num:
            right = mid - 1
        
        else:
            left = mid + 1
            
    return -1
    
if __name__ == '__main__':
    ls = [1,2,3,4,22,33,44,55,66]
    num = 33
    index = search(num, ls)
    if index != -1:
        print(f"find the number at index {index}")
    else:
        print("Can't find")