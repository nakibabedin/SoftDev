#first_last6
def first_last6(nums):
    #function returns true if 6 appears as EITHER the first or last element in an array    
    return nums[0]==6 or nums[-1]==6
    
print(first_last6([1, 2, 6])) #→ True
print(first_last6([6, 1, 2, 3]))# → True
print(first_last6([13, 6, 1, 2, 3]))# → False

#same_first_last
def same_first_last(nums):
    #function returns true if the length of the array is greater than or equal to 1, and the first element of the array equals to the last
    return len(nums)>=1 and nums[0]==nums[-1]

print(same_first_last([1, 2, 3])) #F
print(same_first_last([1, 2, 3, 1])) #T
print(same_first_last([1, 2, 1])) #T

#make_pi
def make_pi():
    #returns first 3 digits of pi
    return [3,1,4]

print(make_pi()) #[3, 1, 4]

#common_end
def common_end(a, b):
    #function returns true if either the first elements of a and b are equal, or the last elements of a and b are equal
    return a[0]==b[0] or a[-1]==b[-1]

print(common_end([1,2,3],[7,3])) #True
print(common_end([1, 2, 3], [7, 3, 2])) #False
print(common_end([1, 2, 3], [1, 3])) #True

#sum3
def sum3(nums):
    #function returns sum of the elements in a 3-element list
    return nums[0]+nums[1]+nums[2]

print(sum3([1, 2, 3])) #6
print(sum3([5, 11, 2])) #18
print(sum3([7, 0, 0])) #7

#rotate_left3
def rotate_left3(nums):
    #function returns a new list with the original list rotated left
    res = [nums[1], nums[2], nums[0]]
    return res

print(rotate_left3([1, 2, 3])) #[2, 3, 1]
print(rotate_left3([5, 11, 9])) #[11, 9, 5]
print(rotate_left3([7, 0, 0])) #[0, 0, 7]

#reverse3
def reverse3(nums):
    #function returns a new list with the original list reversed
    res = [nums[2], nums[1], nums[0]]
    return res

print(reverse3([1, 2, 3])) #[3, 2, 1]
print(reverse3([5, 11, 9])) #[9, 11, 5]
print(reverse3([7, 0, 0])) #[0, 0, 7]

#max_end3
def max_end3(nums):
    #function figures out the bigger number of the first and last elements of the array, and transforms the 3-element list to consist only of that bigger number
    big = max(nums[0], nums[2])
    return [big, big, big]

print(max_end3([1, 2, 3])) #[3, 3, 3]
print(max_end3([11, 5, 9])) #[11, 11, 11]
print(max_end3([2, 11, 3])) #[3, 3, 3]

#sum2
def sum2(nums):
    #function returns sum of first 2 elements in the array. special cases: if length of arr is 0, return 0. if length is less than 2, return the element in the list
    if (len(nums) < 2):
        if (len(nums) == 0):
            return 0
        return nums[0]
    return nums[0] + nums[1]

print(sum2([1, 2, 3])) #3
print(sum2([1, 1])) #2
print(sum2([1, 1, 1, 1])) #2

#middle_way
def middle_way(a, b):
    #function returns a new list of length 2, consisting of the middle elements of lists a and b, each of length 3
    return [a[1], b[1]]

print(middle_way([1, 2, 3], [4, 5, 6])) #[2, 5]
print(middle_way([7, 7, 7], [3, 8, 0])) #[7, 8]
print(middle_way([5, 2, 9], [1, 4, 5])) #[2, 4]

#make_ends
def make_ends(nums):
    #function returns a new list of length 2, consisting of the first and last elements of original list which will always be length 1 or more
    return [nums[0], nums[-1]]

print(make_ends([1, 2, 3])) #[1, 3]
print(make_ends([1, 2, 3, 4])) #[1, 4]
print(make_ends([7, 4, 6, 2])) #[7, 2]

#has23
def has23(nums):
    #function returns true if list of length 2 contains either a 2 or a 3, false otherwise
    return (nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3)

print(has23([2, 5])) #True
print(has23([4, 3])) #True
print(has23([4, 5])) #False