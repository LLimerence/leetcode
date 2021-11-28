# 26. 删除有序数组中的重复项

# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
def remove(nums):
    slow, fast = 0,0
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            slow = slow + 1
            nums[slow] = nums[fast]

        fast = fast+1
    return slow+1
remove([1, 1, 2])
# 283. 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]

def pop(nums):
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[fast] !=0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow+=1
        fast+=1
    return nums

