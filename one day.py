#  704.二分查找
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
# 示例 1:输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
# 示例 2:输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1

def rightclose(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:   # 左闭右闭
        mid = (l+r)//2
        if nums[mid] < target:
            l = mid+1
        elif nums[mid] > target:
            r = mid-1
        else:
            return mid
    return -1
def rightopen(nums, target):
    l, r = 0, len(nums)
    while l < r:   # 左闭右开
        mid = (l+r)//2
        if nums[mid] < target:
            l = mid+1
        elif nums[mid]> target:
            r = mid
        else:
            return mid
    return -1

# 35.搜索插入位置
#给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。你可以假设数组中无重复元素。

#示例 1:[1,3,5,6], 5
#输出: 2
# 示例 2: 输入: [1,3,5,6], 2
# 输出: 1

def serch(nums, target):
    left, right = 0, len(nums)-1 # 右关闭
    while left <= right:
        middle = (left+(right-left))//2 # 防止内存溢出
        if nums[middle] < target:
            left = middle+1
        elif nums[middle] > target:
            right = middle-1
        else:
            return middle
    return left
if __name__ =="__main__":
    nums = [int(i) for i in input().split(" ")]
    print(nums)
    target = int(input())
    # nums = [-1, 0, 3, 5, 9, 12]
    # target = 9
    serch(nums, target)





