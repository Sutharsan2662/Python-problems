def twoSum(nums, target):
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                list_i = [i]
                list_j = [j]
                list = list_i + list_j
                print(list)
            else:
                continue
    

nums = [2,11,7,15]
target = 9 
print(twoSum(nums, target))

