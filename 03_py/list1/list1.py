#first_last6
def first_last6(nums):
    return nums[0]==6 or nums[-1]==6
    
print(first_last6([1, 2, 6])) #→ True
print(first_last6([6, 1, 2, 3]))# → True
print(first_last6([13, 6, 1, 2, 3]))# → False

#same_first_last
def same_first_last(nums):
    return len(nums)>=1 and nums[0]==nums[-1]

print(same_first_last([1, 2, 3])) #F
print(same_first_last([1, 2, 3, 1])) #T
print(same_first_last([1, 2, 1])) #T

#make_pi
def make_pi():
    return [3,1,4]

