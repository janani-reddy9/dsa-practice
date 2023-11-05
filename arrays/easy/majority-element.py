def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    data = {}
    for i in nums:
        if i not in data:
            data[i] = 1
        else:
            data[i] += 1
    maxValue = 0
    maxIndex = 0
    for val in data.keys():
        if maxValue < data[val]:
            maxValue = data[val]
            maxIndex = val
    return maxIndex


print(majorityElement([3, 2, 3]))
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
