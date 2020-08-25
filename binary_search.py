import math

def binary_search(x, nums):
    ### return the list index of given value in list ###
    found = False
    # define initial ranges
    low = 0
    mid = math.ceil(len(nums)/2)
    high = len(nums)-1

    if not x in nums:
        print(f'{x} is not in the given list')
        return
    while not found:
        # test to see if any predefined values are the correct guess
        if x == nums[low] or x == nums[mid] or x == nums[]:
            print(f'{x} is in postion {low}')
            found = True
        elif x == nums[mid]:
            print('You found it!')
            found = True
        elif x == nums[high]:
            print('You found it!')
            found = True
        
        # Update ranges to tighten the search
        elif x > nums[mid]:
            print('x is greater than mid')
            low = mid
            mid = math.ceil((high-mid)/2)
        else:
            print('x is less than mid')
            high = mid
            mid = math.floor((mid-low)/2)
        
        print(f'High = {nums[high]}')
        print(f'Mid = {nums[mid]}')
        print(f'Low = {nums[low]}')
    

binary_search(3, [1,3,4,5,7,9,10,12,15,20,21,22,24,27,30,35])