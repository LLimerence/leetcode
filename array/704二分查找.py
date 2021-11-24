# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
#
# 示例 1:
#
# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
# 示例 2:
#
# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1

def serch(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:   # 左闭右闭
        mid = (l+r)//2
        if nums[mid] < target:
            l = mid+1
        elif nums[mid]> target:
            r = mid-1
        else:
            return mid
    return -1

def serch(nums, target):
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
if __name__ =="__main__":
    # nums = [int(i) for i in input().split(" ")]
    # print(nums)
    # target = int(input())
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    x = serch(nums, target)
    print(x)




