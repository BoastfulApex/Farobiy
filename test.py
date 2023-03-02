def twoSum(nums, target):
    prev = {} 
        
    for i, n in enumerate(nums):
        print(i)
        print(n)
        diff = target - n
        if diff in prev:
            return [prev[diff], i]
        prev[n] = i
    return

print(twoSum([2,11,7,15], 9))