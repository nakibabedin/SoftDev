#count_evens
def count_evens(nums):
    #function returns a counter of even number in the list
    counter=0
    for x in range(len(nums)):
        if (nums[x]%2==0):
            counter+=1
    return counter

print(count_evens([2, 1, 2, 3, 4])) #3
print(count_evens([2, 2, 0])) #3
print(count_evens([1, 3, 5])) #0

#big_diff
def big_diff(nums):
    #function returns the range of the list(largest - smallest)	
    largest=nums[0]
    smallest=nums[0]
    for x in range(len(nums)):        
        largest = max(nums[x], largest)
        smallest = min(nums[x], smallest)
    return largest-smallest

print(big_diff([10, 3, 5, 6])) #7
print(big_diff([7, 2, 10, 9])) #8
print(big_diff([2, 10, 7, 2])) #8

#centered_average
def centered_average():
    #function returns the average of the list, excluding the outliers(largest and smallest values)
    big = max(nums)
    small = min(nums)
    nums.remove(big)
    nums.remove(small)
    return sum(nums)/len(nums)

print(centered_average([1, 2, 3, 4, 100])) #3
print(centered_average([1, 1, 5, 5, 10, 8, 7])) #5
print(centered_average([-10, -4, -2, -4, -2, 0])) #-3

#sum13
def sum13(nums):
    #function returns the sum of the elements in the list, excluding 13s and the numbers immediately following them
    summy = 0
    for i in range(len(nums)):
        if ((i == 0 and nums[i] != 13) or (nums[i] != 13 and nums[i-1] != 13)):
        summy += nums[i]
    return summy

print(sum13([1, 2, 2, 1])) #6
print(sum13([1, 1])) #2
print(sum13([1, 2, 2, 1, 13])) #6

#sum67
def sum67(nums):
    #function returns the sum of the elements in the list, excluding sections defined by numbers between a 6 in the list and a 7(6 and 7 also not included in sum)
    summy = 0
    skip = False
    for i in range(len(nums)):
        if (nums[i] == 6):
        skip = True
        if (skip and nums[i] == 7):
            skip = False
            continue
        if not skip:
            summy += nums[i]
    return summy

print(sum67([1, 2, 2])) #5
print(sum67([1, 2, 2, 6, 99, 99, 7])) #5
print(sum67([1, 1, 6, 7, 2])) #4

#has22
def has22(nums):
    #function returns True if list has two consecutive 2s at any point, false otherwise
    for i in range(len(nums) - 1):
    if (nums[i] == 2 and nums[i+1] == 2):
        return True
    return False

print(has22([1, 2, 2])) #True
print(has22([1, 2, 1, 2])) #False
print(has22([2, 1, 2])) #False
        
