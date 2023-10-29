"""
https://leetcode.com/problems/merge-sorted-array/
"""


def merge(nums1, m, nums2, n):
    """
    * This doesn't work because we have to replace nums1 inplace, not by inserting value and removing m-n 0's
    """
    m_minus_n = len(nums1) - n
    lennums1 = len(nums1)
    i = 0
    j = 0
    c = 0
    while j < n:
        if i == m_minus_n + c:
            i = m_minus_n + c
            while j < n:
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
                c += 1
            break
        if nums1[i] < nums2[j]:
            i += 1
        else:
            nums1.insert(i, nums2[j])
            j += 1
            i += 1
            c += 1
    nums1 = nums1[0:lennums1]
    print(nums1)


def merge_1(nums1, m, nums2, n):
    nums1Index = len(nums1) - 1
    i = m - 1
    j = n - 1
    if i == -1:
        while j > -1:
            nums1[j] = nums2[j]
            j -= 1
    while i > -1 and j > -1:
        if nums1[i] > nums2[j]:
            nums1[nums1Index] = nums1[i]
            i -= 1
        else:
            nums1[nums1Index] = nums2[j]
            j -= 1
        nums1Index -= 1
        if j == -1:
            break
        if i ==  -1 and j != -1:
            while j > -1:
                nums1[j] = nums2[j]
                j -= 1
    return nums1


print(merge_1([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(merge_1([0,0], 2, [1,2], 2))
