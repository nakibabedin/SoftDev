#count_evens
def count_evens(nums):
    counter=0
    for x in range(len(nums)):
        if (nums[x]%2==0):
            counter+=1
    return counter

#big_diff
def big_diff(nums):
    largest=nums[0]
    smallest=nums[0]
    for x in range(len(nums)):
        largest = max(nums[x], largest)
        smallest = min(nums[x], smallest)
    return largest-smallest

#centered_average
def centered_average():
    
